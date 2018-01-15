# LanguageCrunch NLP Service docker image

- Sentence detection
- Tokenization


## Sentiment

`sentence: "RT @Slate: Donald Trump's administration: "Government by the worst men."",`
```json
 sentiment: {
   polarity: -1,
   subjectivity: 1
 },
 .....  // removed for brevity
 entities: [
 {
   text: "Donald Trump's administration",
   label: "PERSON"
 }
]
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


## Sentence type detection
- assertive
- interrogative
- exclamatory
- negative

## Relation extraction


`Eg: The currency of India is Rupees.`
```
{
   subject: "The currency",
   object: "India",
   relation: "GPE"
 }
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
 
 
## Endpoints

- Sentence parse 

  `GET http://localhost:8080/nlp/parse?sentence=<Sentences>`
- Word lookup 

  `GET http://localhost:8080/nlp/word?word=ask&pos=v`

- Coreference resolution 

  `GET http://localhost:8080/nlp/coref?sentence=<Sentences>`