import re
f = open("mobydick.txt")
data = f.read()
print("\nReading mobydick.txt\n")

#prints the number of words, punctions, and symbols that appear in the text
print("number of words")
print(len(data))

#sorts the number of distinct words .ie tokens
sorted(set(data))

#to get the number of distinct words
print("number of distinct words")
print(len(set(data)))