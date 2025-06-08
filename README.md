# TC2037-Evidenge-2-Generating-and-Cleaning-a-Restricted-Context-Free-Grammar
## Description
The language I chose to model consists of simple sentences in Portuguese that follow the next structure:

Pronoun + Verb + Article/Determiners + Noun 

The sentences follow strictly that order, without punctuation marks, conjuctions, or any other additional elements.
The purpose of this evidence is to model basic Portuguese sentences that are used everyday and that are simple enough to parse and analyze with a context free grammar.

## Model of the Solution
The grammar that recognizes the language is the following:

S → NP VP  
NP → P  
VP → V DetP  
DetP → Det N  
P → eu | tu | ele | ela | nós | vocês | eles  
V → come | bebe | ama | vê  
Det → o | a | os | as  
N → pão | água | futebol | filme  

Where:
- S: represents the entire sentence.
- NP (NounPhrase): reresnts the subject and consists of a Pronoun
- VP (VerbPhrase): represents the action and the object and consists of a Verb followed by an Article Phrase
- DetP (DeterminerPhrase): represents the object and consists of an Determiner and a Noun.

  Here are examples of valid sentences this grammar can generate:

- eu come o pão
- ela bebe a água
- nós ama o futebol
- vocês vê o filme
- eles come o filme

All sentences must follow this order. If the structure is altered or if a word is out of place, the sentence will be rejected


This structure is to keep the model context-free and suitable for LL(1) parsing after eliminating ambiguity and left recursion.

The syntactic tree of the sentence "eu come o pào" is the following:
(S (NP (P eu)) (VP (V come) (DetP (Det o) (N pão))))
![Diagrama en blanco (1)](https://github.com/user-attachments/assets/2dc9787a-f2de-4bd8-90be-01cd11efada4)

## Ambiguity and Left Recursion Analysis

This grammar is not ambiguous since each sentence can only be derived in **one** unique way, and each word generates a **single** valid parse tree. There is no possibility of multiple parse trees for the same sentence since they all follow the simple structure subject-verb-object.

Regarding left recursion, the grammar does not contain it. All productions start with terminal symbols or non-terminals that eventually lead directly to terminal symbols without recursion.

Therefore, the grammar is suitable for LL(1) parsing.

However, it is important to consider how ambiguity could arise if additional production rules were added.

For example, if we modified the grammar so that a Pronoun could also be interpreted as a Noun, introducing a new production like:
```
N → pão | água | futebol | filme | eu | tu
```
In this case, the word "eu" ("I" in Portuguese) could be parsed both as a Pronoun (P) and as a Noun (N), leading to two possible parse trees for a sentence like "eu come o pão"
**Parse 1**
```
(S (NP (P eu)) (VP (V come) (DetP (Det o) (N pão))))
```
**Parse 2** Eu as a NOUN.
```
(S (NP (N eu)) (VP (V come) (DetP (Det o) (N pão))))
```
This ambiguity would make the grammar unsuitable for LL(1) parsing, because the parser would not know whether "eu" should be interpreted as a Pronoun or as a Noun.

Fortunately, in the original design of the grammar, this does not happen.


## Implementation
The grammar was implemented using the natural language toolkit (nltk) library. If you don't have it installed, you can install it using the following command:
```
pip install nltk
```
Once installed you can run the program as usual.

The grammar was defined using the "CFG.fromstring()" function from the nltk library which allows us to parse grammars from strings.
```
portuguese = CFG.fromstring("""
S -> NP VP  
NP -> P  
VP -> V DetP  
DetP -> Det N  
P -> 'eu' | 'tu' | 'ele' | 'ela' | 'nós' | 'vocês' | 'eles'  
V -> 'come' | 'bebe' | 'ama' | 'vê'  
Det -> 'o' | 'a' | 'os' | 'as'  
N -> 'pão' | 'água' | 'futebol' | 'filme'           
""")
```
I also used the "ChartParser" function with the defined grammar which efficiently parse context free grammars by building parse trees dinamically.
```
parser = nltk.ChartParser(portuguese)
```
Then I defined a "test-sentence(sentence) function that tokinizes the input sentence, parses it using the grammar, and returns whether the sentence was accepted or not.
```
def test_sentence(sentence):
    sent = sentence.split()

    # Create a Chart Parser for better handling of the grammar
    parser = nltk.ChartParser(portuguese)

    # Print the syntax tree of each accepted sentence
    trees = list(parser.parse(sent))
    if trees:
        for tree in trees:
            print(tree)
        return True
    else:
        return False
```
In case the sentence is accepted, the corresponding syntactic tree is printed next to it to visualize the structure according to the defined grammar.  
Output of an accepted sentence:
```
(S (NP (P eles)) (VP (V come) (DetP (Det o) (N filme))))
eles come o filme: Accepted
```
Output of a Rejected sentence:
```
eu filme vê as: Rejected
```
When you run the program it will automatically test all the predefined sentences, print the corresponding syntactic tree and print whether the sentence was Accepted or Rejected.

## Tests
To validate the grammar I implemented a set of tests that you can find on the *grammar.py* file in this repository. This set of tests includes both correctly structured sentences that return "Accepted" and incorrectly structured sentences that return "Rejected".  

**Correct Sentences:**
Eu come o pão, ela bebe a água, nós ama o futebol, vocês vê o filme, eles come o filme.

**Incorrect Sentences:**
bebe tu os futebol, água bebe a tu, eu filme vê as, es pão come a, elle ama futebol.

### LL1 Parsing Example
Here are some parse trees for some of the valid sentences, showing the output of the program:

Eu come o pão
```
          S
         / \
       NP   VP
       |    / \
      Eu   V   DetP
           |   / \
         come D  N
              |   |
              o  pão

```

Ela bebe a água
```
          S
         / \
       NP   VP
       |    / \
     Ela   V   DetP
           |   / \
         bebe D  N
              |   |
              a  água

```
Nós ama o futebol
```
          S
         / \
       NP   VP
       |    / \
     Nós   V   DetP
           |   / \
          ama D  N
              |   |
              o  futebol
```



This grammar **only** validates the syntactic structure of sentences according to the context-free rules.

I implemented a `run_tests()` function that automatically checks multiple valid and invalid sentences. The output shows whether each sentence was accepted or rejected, and if the result matches the expected outcome.

This confirms that the grammar works as intended and follows the designed rules strictly.

## Analysis

### Chomsky Hierarchy Classification
According to Chomsky's hierarchy, the grammar is a **Context-Free (Type 2)**.  
In a context-free grammar, a single non-terminal can be replaced by a group of terminals and/or non-terminals. The left part of the rule always has only one non-terminal, and the right part shows what non-terminal can become.

Because there were **no ambiguities** or **left recursion** detected in the original grammar, the grammar remains classified as **Context-Free (Type 2)** after the analysis.

### Time Complexity Implications

Parsing context-free grammars using Chart Parsing has a time complexity of **O(n³)** in the worst case, where n is the number of words in the sentence.

### Time Implications and Examples of Chomsky Hierarchy Levels

**Regular Grammars (Type 3):**  
- Parsing/recognition is very efficient, typically O(n) (linear) time complexity, where n is the length of the input string.
- Example of application: Simple patterns, such as identifiers or sequences matching regular expressions.
- String Example: "abab", "abc123"

**Context-Free Grammars (Type 2):**  
- Parsing is generally more complex than regular languages, with a typical time complexity of O(n³) (polynomial) using general parsing algorithms like CYK or Chart Parsing.
- Example of application: Programming languages syntax (balanced parentheses, nested structures).
- String Example: "eu come o pão"
  
**Context-Sensitive Grammars (Type 1):**  
- Parsing is more complex and usually NP-complete; recognizing context-sensitive languages can take exponential time in the worst case.
- Example of application: Parts of natural languages where agreement between words must be enforced (subject-verb agreement).
- String Example: "Nós comemos o pão" (requiring subject-verb agreement)

**Recursively Enumerable Grammars (Type 0):**  
- Parsing is undecidable; there is no general algorithm that always finishes. Computations may never terminate.
- Example of application: General mathematical theories, Turing machine languages.
- String Example: Languages that can only be recognized by a Turing machine, could not find any example that I understood.


## Resources 

- Bird, Steven, Edward Loper and Ewan Klein (2009), Natural Language Processing with Python. O’Reilly Media Inc.

- NLTK :: Sample usage for grammar. (n.d.). https://www.nltk.org/howto/grammar.html

- 8.Errors and exceptions. (n.d.). Python Documentation. https://docs.python.org/3/tutorial/errors.html#handling-exceptions

- 8.Analyzing sentence structure. (n.d.). https://www.nltk.org/book/ch08.html
