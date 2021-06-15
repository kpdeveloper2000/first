import nltk
groucho_grammar = nltk.CFG.fromstring("""
S -> NP VP
PP -> P NP
NP -> Det N | Det N PP | 'i'
VP -> V NP | VP PP
Det -> 'an' | 'my' | 'the'
N -> 'bird' | 'grain' | 'dog' | 'lazy'
V -> 'pecks' | 'jumps' | 'see'
P -> 'in' | 'over'
""")
# taking input from the user
data = input("Enter sentence: ")
# spliting the given sentence
data = list(data.split())
sent = []
# looping through data and appneding it to the sent
for word in data:
    sent.append(word.lower())
# deciding the edges to add to the graph using chart parser
parser = nltk.ChartParser(groucho_grammar)
# printing the parser element
for tree in parser.parse(sent):
    print(tree)
