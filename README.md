# TC2037-Evidenge-2-Generating-and-Cleaning-a-Restricted-Context-Free-Grammar
## Description
The language I chose to model consists of simple sentences in Portuguese that follow the next structure:

Pronoun + Verb + Article + Noun 

The sentences follow strictly that order, without punctuation marks, conjuctions, or any other additional elements.
The purpose of this evidence is to model basic Portuguese sentences that are used everyday and that are simple enough to parse and analyze with a context free grammar.
## Model of the Solution
The grammar that recognizes the language is the following:

S → NP VP  
NP → P  
VP → V AP  
AP → A N  
P → eu | tu | ele | ela | nós | vocês | eles  
V → come | bebe | ama | vê  
A → o | a | os | as  
N → pão | água | futebol | filme  

Where:
- S: represents the entire sentence.
- NP (NounPhrase): reresnts the subject and consists of a Pronoun
- VP (VerbPhrase): represents the action and the object and consists of a Verb followed by an Article Phrase
- AP (ArticlePhrase): represents the object and consists of an Article and a Noun.


This structure is to keep the model context free and suitable for LL(1) parsing after eliminating ambiguity and left recursion.

The syntatic tree of the sentence "eu come o pào" is the following:
![Diagrama en blanco (1)](https://github.com/user-attachments/assets/2dc9787a-f2de-4bd8-90be-01cd11efada4)
