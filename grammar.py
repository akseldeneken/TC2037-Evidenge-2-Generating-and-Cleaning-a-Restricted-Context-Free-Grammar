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
VP -> V AP  
AP -> A N  
P -> 'eu' | 'tu' | 'ele' | 'ela' | 'nós' | 'vocês' | 'eles'  
V -> 'come' | 'bebe' | 'ama' | 'vê'  
A -> 'o' | 'a' | 'os' | 'as'  
N -> 'pão' | 'água' | 'futebol' | 'filme'           
""")


def test_sentence(sentence):
    sent = sentence.split()

    # Create a Chart Parser for better handling of the grammar
    parser = nltk.ChartParser(portuguese)

    # Print the syntax tree of each accepted sentence
    for tree in parser.parse(sent):
        print(tree)

    # Check if its a valid sentence
        trees = list(parser.parse(sent))
        if len(trees) > 0:
            return True
        else:
            return False


def main():
    # Sentences to test the grammar 
    sentences = [
            "eu come o pão",
            "ela bebe a água",
            "nós ama o futebol",
            "vocês vê o filme",
            "eles come o filme",
            "bebe tu os futebol", # Incorrect
            "água bebe a tu",  # Incorrect
            "eu filme vê as",  # Incorrect
            "es pão come a", # Incorrect
            "elle ama futebol"   # Incorrect
        ]

    # Itirate over each predefined sentence and test it with the grammar "test_sentence(sent)"
    for sent in sentences:
        result = test_sentence(sent)
        if result:
            print(f"{sent}: Accepted\n")
        else:
            print(f"{sent}: Rejected\n")

main()
