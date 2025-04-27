# TC2037-Evidenge-2-Generating-and-Cleaning-a-Restricted-Context-Free-Grammar
## Description
The language I chose to model consists of simple sentences in Portuguese that follow the next structure:
Pronoun + Verb + Article + Noun 
The sentences follow strictly that order, without punctuation marks, conjuctions, or any other additional elements.
The purpose of this evidence is to model basic Portuguese sentences that are used everyday and that are simple enough to parse and analyze with a context free grammar.
## Model of the Solution
The grammar that recognizes the language is the following:
```
S -> Pronoun Verb Article Noun Pronoun
```
