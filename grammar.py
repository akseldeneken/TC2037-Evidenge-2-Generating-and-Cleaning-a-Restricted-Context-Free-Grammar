"""
Aksel Deneken Maldonado A01711966
28/04/2025
TC2037 Evidence 2
The purpose of this project is to model and validate 
simple Portuguese sentences using a context-free grammar.

"""

import nltk
from nltk import CFG


# Define the portuguese grammar after eliminating ambiguity and left recursion
# Create the CFG from string
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


def run_tests():
    valid_sentences = [
        "eu come o pão",
        "ela bebe a água",
        "nós ama o futebol",
        "vocês vê o filme",
        "eles come o filme"
    ]

    invalid_sentences = [
        "bebe tu os futebol",
        "água bebe a tu",
        "eu filme vê as",
        "as pão come a",
        "ele ama futebol"
    ]

    print("---- Valid Sentences ----")
    for sentence in valid_sentences:
        result = test_sentence(sentence)
        print(f"{sentence} | Expected: True | Result: {result} | Test: {'Passed' if result else 'Failed'}\n")

    print("---- Invalid Sentences ----")
    for sentence in invalid_sentences:
        result = test_sentence(sentence)
        print(f"{sentence} | Expected: False | Result: {result} | Test: {'Passed' if not result else 'Failed'}\n")

if __name__ == "__main__":
    run_tests()

