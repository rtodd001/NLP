import re
from nltk.corpus import PlaintextCorpusReader
corpus_root = './texts/'
wordlist = PlaintextCorpusReader(corpus_root, '.*')
print(wordlist.fileids())

#numbr of words
print(len(wordlist.words('mobydick.txt')))
#number of sentences
print(len(wordlist.sents('mobydick.txt')))

print(len(re.findall("\bIshmael\b", './texts/mobydick.txt')))
