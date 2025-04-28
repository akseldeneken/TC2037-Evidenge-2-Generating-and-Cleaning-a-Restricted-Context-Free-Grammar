import nltk
from nltk import CFG

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
    parser = nltk.ChartParser(portuguese)
    for tree in parser.parse(sent):
        print(tree)
        trees = list(parser.parse(sent))
        if len(trees) > 0:
            return True
        else:
            return False


def main():
    sentences = [
            "eu come o pão",
            "ela bebe a água",
            "nós ama o futebol",
            "vocês vê o filme",
            "eles come o filme",
            "bebe tu os futebol", # Incorrect
            "água bebe a tu",  # Incorrect
            "eu filme vê as"  # Incorrect
        ]

    for sent in sentences:
        result = test_sentence(sent)
        if result:
            print(f"{sent}: Accepted\n")
        else:
            print(f"{sent}: Rejected\n")

main()