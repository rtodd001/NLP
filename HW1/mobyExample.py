import re
from nltk.corpus import PlaintextCorpusReader
corpus_root = './texts/'
wordlist = PlaintextCorpusReader(corpus_root, '.*')
print(wordlist.fileids())

#numbr of words
print(len(wordlist.words('mobydick.txt')))
#number of sentences
print(len(wordlist.sents('mobydick.txt')))

#stores a fileobject into f
f = open("./texts/mobydick.txt")
#stores a string into data from f
data = f.readlines()
#corpus is now a giant string delimited by newline character
corpus = "\n".join(data)
#prints the number of times Ishmael appears in the file.
print(len(re.findall(r"\bIshmael\b", corpus)))
