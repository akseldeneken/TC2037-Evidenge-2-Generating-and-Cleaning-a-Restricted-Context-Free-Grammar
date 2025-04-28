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


This structure is to keep the model context-free and suitable for LL(1) parsing after eliminating ambiguity and left recursion.

The syntactic tree of the sentence "eu come o pào" is the following:
(S (NP (P eu)) (VP (V come) (AP (A o) (N pão))))
![Diagrama en blanco (1)](https://github.com/user-attachments/assets/2dc9787a-f2de-4bd8-90be-01cd11efada4)

## Ambiguity and Left Recursion Analysis

This grammar is not ambiguous since each sentence can only be derived in **one** unique way, and each word generates a **single** valid parse tree. There is no possibility of multiple parse trees for the same sentence.

Regarding left recursion, the grammar does not contain it. All productions start with terminal symbols or non-terminals that eventually lead directly to terminal symbols without recursion.

Therefore, the grammar is suitable for LL(1) parsing.

## Implementation
The grammar was implemented using the natural language toolkit (nltk) library. If you don't have it installed, you can install it using the following command:
```
pip install ntlk
```
Once installed you can run the program as usual.

The grammar was defined using the "CFG.fromstring()" function from the ntlk library which allows us to parse grammars from strings.
```
portuguese = CFG.fromstring("""
S -> NP VP  
NP -> P  
VP -> V AP  
AP -> A N  
P -> 'eu' | 'tu' | 'ele' | 'ela' | 'nós' | 'vocês' | 'eles'  
V -> 'come' | 'bebe' | 'ama' | 'vê'  
A -> 'o' | 'a' | 'os' | 'as'  
N -> 'pão' | 'água' | 'futebol' | 'filme'           
""")
```
I also used the "ChartParser" function with the defined grammar which efficiently parse context free grammars by building parse trees dinamically.
```
parser = nltk.ChartParser(portuguese)
```
Then I defined a "test-sentence(sentence) function that tokinizes the input sentence, parses it using the grammar, and returns wether the sentence was accepted or not.
```
def test_sentence(sentence):
    sent = sentence.split()
    parser = nltk.ChartParser(portuguese)
    for tree in parser.parse(sent):
        print(tree)
        trees = list(parser.parse(sent))
        if len(trees) > 0:
            return True
        else:
            return False
```
In case the sentence is accepted, the corresponding syntactic tree is printed next to it to visualize the structure according to the defined grammar.  
Output of an accepted sentence:
```
(S (NP (P eles)) (VP (V come) (AP (A o) (N filme))))
eles come o filme: Accepted
```
Output of a Rejected sentence:
```
eu filme vê as: Rejected
```
When you run the program it will automatically test all the predefined sentences, print the corresponding syntactic tree and print whether the sentence was Accepted or Rejected.

## Tests
To validate the grammar I implemented a set of tests that you can find on the .py file in this repository. This set of tests includes both correctly structured sentences that return "Accepted" and incorrectly structured sentences that return "Rejected".  
Examples:  
"ela bebe a água" was accepted since it has a correct structure.  
"água bebe a tu" was rejected since it has an incorrect structure.  

This grammar **only** validates the syntactic structure of sentences according to the context-free rules.

## Analysis

### Chomsky Hierarchy Classification
According to Chomsky's hierarchy, the grammar is a **Context-Free (Type 2)**.  
In a context-free grammar, a single non-terminal can be replaced by a group of terminals and/or non-terminals. The left part of the rule always has only one non-terminal, and the right part shows what non-terminal can become.

Because there were **no ambiguities** or **left recursion** detected in the original grammar, the grammar remains classified as **Context-Free (Type 2)** after the analysis.

### Time Complexity Implications

Parsing context-free grammars using Chart Parsing has a time complexity of **O(n³)** in the worst case, where n is the number of words in the sentence.


## Resources 

- Bird, Steven, Edward Loper and Ewan Klein (2009), Natural Language Processing with Python. O’Reilly Media Inc.

- NLTK :: Sample usage for grammar. (n.d.). https://www.nltk.org/howto/grammar.html

- 8.Errors and exceptions. (n.d.). Python Documentation. https://docs.python.org/3/tutorial/errors.html#handling-exceptions

- 8.Analyzing sentence structure. (n.d.). https://www.nltk.org/book/ch08.html
