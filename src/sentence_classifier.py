# Classifier classifies given sentence into following types
SENTENCE_TYPE = {
    "ASSERTIVE": "assertive",
    "NEGATIVE""": "negative",
    "INTERROGATIVE": "interrogative",
    "IMPERATIVE": "imperative",
    "EXCLAMATORY": "exclamatory"
}

# list of negative words
negativeWords = [
    "no", "not", "never", "neither", "nobody", "none", "nor",
    "nothing", "nowhere", "few", "hardly", "little", "rarely",
    "scarcely", "seldom", "hadn't", "don't", "doesn't",
    "didn't", "couldn't", "can't", "wouldn't", "haven't", "aren't",
    "hasn't", "won't", "shouldn't", "isn't", "wasn't", "weren't"
]

""""
 * classify the given sentence into types e.g interrogative
 * @param {String} sentence
 * @return {String} type
"""


def SentenceTypeClassifier(doc):
    checkEndMark = True

    if checkEndMark:
        last_token = doc[len(doc) - 1]
        strip = last_token.string.strip()
        if len(strip) > 0:
            strip_ = strip[0]
            endMark = strip_
        else:
            endMark = ""
        if endMark == '.' or endMark == '?' or endMark == '!':
            if endMark == '?':
                return SENTENCE_TYPE["INTERROGATIVE"]
            elif endMark == '!':

                if isImperative(doc):
                    return SENTENCE_TYPE["IMPERATIVE"]
                else:
                    return SENTENCE_TYPE["EXCLAMATORY"]

            else:
                if isImperative(doc):
                    return SENTENCE_TYPE["IMPERATIVE"]

                if isNegative(doc):
                    return SENTENCE_TYPE["NEGATIVE"]
                else:
                    return SENTENCE_TYPE["ASSERTIVE"]

    type = SENTENCE_TYPE["ASSERTIVE"]

    if isInterrogative(doc):
        type = SENTENCE_TYPE["INTERROGATIVE"]
    elif isImperative(doc):
        type = SENTENCE_TYPE["IMPERATIVE"]
    elif isExclamatory(doc):
        type = SENTENCE_TYPE["EXCLAMATORY"]
    elif isNegative(doc):
        type = SENTENCE_TYPE["NEGATIVE"]

    return type


def isNegative(taggedWords):
    for i in range(len(taggedWords)):
        word = taggedWords[i].string.strip().lower()
        for j in range(len(negativeWords)):
            if word == negativeWords[j]:
                return True

        if word == "do" or word == "does" or word == "did":
            if taggedWords[i + 1]:
                nextWord = taggedWords[i + 1].string.strip().lower()
                if nextWord == "n't":
                    return True

    return False


def isImperative(taggedWords):
    firstWord = getWord(taggedWords, 0)
    if firstWord:
        if firstWord == "have":

            # check for 2nd tag, must not be NN/PRP to be imperative
            secondTag = getTag(taggedWords, 1)
            if secondTag:
                if secondTag == "PRP" or secondTag == "NN":
                    return False

    firstRegexRule = [
        ["VB", "VBP"]
    ]
    secondRegexRule = [
        ["NN"],
        [","],
        ["VB", "VBP"]
    ]
    thirdRegexRule = [
        ["RB"],
        ["VB", "VBP"]
    ]
    fourthRegexRule = [
        ["NN"],
        [","],
        ["RB"],
        ["VB", "VBP"]
    ]
    imperative = False
    if isMatchingRegex(firstRegexRule, taggedWords):
        imperative = True
    elif isMatchingRegex(secondRegexRule, taggedWords):
        imperative = True
    elif isMatchingRegex(thirdRegexRule, taggedWords):
        imperative = True
    elif isMatchingRegex(fourthRegexRule, taggedWords):
        imperative = True

    return imperative


def isInterrogative(taggedWords):
    firstRegexRule = [
        ["MD", "VBP", "VBZ", "VBD"],
        ["PRP", "NN", "NNP", "NNS", "VBG"]
    ]
    secondRegexRule = [
        ["WRB", "WP"],
        ["MD", "VBP", "VBZ", "VBD"]
    ]
    thirdRegexRule = [
        ["MD", "VBP", "VBZ", "VBD"],
        ["DT"],
        ["PRP", "NN", "NNP", "NNS", "VBG"]
    ]
    interrogative = False
    if isMatchingRegex(firstRegexRule, taggedWords):
        interrogative = True
    elif isMatchingRegex(secondRegexRule, taggedWords):
        interrogative = True
    elif isMatchingRegex(thirdRegexRule, taggedWords):
        interrogative = True

    return interrogative


def isExclamatory(taggedWords):
    firstRegexRule = [
        ["UH"]
    ]
    exclamatory = False
    if isMatchingRegex(firstRegexRule, taggedWords):
        exclamatory = True

    return exclamatory


def getTag(taggedWords, position):
    tag = None
    if position < len(taggedWords) and taggedWords[position]:
        tag = taggedWords[position].tag_
    return tag


def getWord(taggedWords, position):
    if len(taggedWords) > position and taggedWords[position]:
        word = taggedWords[position].string.strip().lower()
    return word


def isMatchingRegex(regexArray, taggedWords):
    match = True
    for position in range(len(regexArray)):
        innerArray = regexArray[position]
        tag = getTag(taggedWords, position)

        # end of sentence, no need to further match regex pattern rule
        if not tag:
            break

        innerMatch = False
        for i in range(len(innerArray)):
            expectedTag = innerArray[i]
            if tag == expectedTag:
                innerMatch = True
                break

        if not innerMatch:
            match = False
            break

    return match
