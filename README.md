# LanguageCrunch NLP Service docker image

Docker image 
https://hub.docker.com/r/artpar/languagecrunch/


## Sentiment

`sentence: The new twitter is so weird. Seriously. Why is there a new twitter? What was wrong with the old one? Fix it now.`
```json
{
  "relations": [],
  "sentences": [
    {
      "sentence": "The new twitter is so weird. ",
      "sentence_type": "assertive",
      "sentiment": {
        "polarity": -0.18181818181818182,
        "subjectivity": 0.7272727272727273
      },
      "root": {
        "text": "is ",
        "orth": 2
      },
      "pos": [
        {
          "text": "The new twitter",
          "lemma": "the",
          "pos": "DET",
          "tag": "DT",
          "dep": "nsubj",
          .
          .
          .
```

## Entity extraction

- PERSON
- NORP
- FACILITY
- ORG
- GPE
- LOC
- PRODUCT
- EVENT
- WORK_OF_ART
- LAW
- LANGUAGE
- DATE
- TIME
- PERCENT
- MONEY
- QUANTITY
- ORDINAL
- CARDINAL

`Eg: Bill Gates, the founder of Microsoft, hosted a party last night`
```json
  "entities": [
    {
      "text": "Bill Gates",
      "label": "PERSON"
    },
    {
      "text": "Microsoft",
      "label": "ORG"
    },
    {
      "text": "last night",
      "label": "TIME"
    }
  ]
}
```

## Sentence type detection
- assertive
- interrogative
- exclamatory
- negative

## Relation extraction


`Eg: Bill Gates, the founder of Microsoft, hosted a party last night`
```
  "relations": [
    {
      "subject": "the founder",
      "object": "Microsoft",
      "relation": "ORG"
    }
  ],
```


`Eg: Apple is looking at buying U.K. startup for $1 billion`
```[
 {
   subject: "N/A",
   object: "U.K. startup",
   relation: "GPE"
 },
 {
   subject: "buying",
   object: "$1 billion",
   relation: "MONEY"
 }
],

```


## Word look up

- Category of word 
  - Hypernyms - **colour** is a hypernym of **red**.
- Specific words of a category 
  - Holonyms - **red** is a holonym of **color**
- Synonyms to match
- Examples
- Word frames ( how the word is used )
 
- Coreference resolution
- Pronouns/references to nouns


`Eg: startle, verb` 
 
```json
  "results": [
    {
      "definition": "to stimulate to action",
      "examples": [
        "..startled him awake",
        "galvanized into action"
      ],
      "lemma_names": [
        "startle",
        "galvanize",
        "galvanise"
      ],
      "hypernyms": [
        {
          "definition": "surprise greatly; knock someone's socks off",
          "examples": [
            "I was floored when I heard that I was promoted"
          ],
          "lemma_names": [
            "shock",
            "floor",
            "ball_over",
            "blow_out_of_the_water",
            "take_aback"
          ]
        }
      ],
      "lemmas": [
        {
          "frame_strings": [
            "Somebody startle somebody",
            "Something startle somebody",
            "Somebody startle somebody into V-ing something"
          ],
```
 
## Endpoints

## Sentence parse [Spacy]

  `GET http://localhost:8080/nlp/parse?sentence=<Sentences>`

## Word lookup [Wordnet]

  `GET http://localhost:8080/nlp/word?word=ask&pos=v`

## Coreference resolution [neuralcoref]

  `GET http://localhost:8080/nlp/coref?sentence=<Sentences>`