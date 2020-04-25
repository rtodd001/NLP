import re
from collections import defaultdict

def ngram(number):
    count = -1
    filename = './mobydick.txt'
    myFile = open(filename)
    text = myFile.read()
    pattern = re.compile(r'\w+')
    full = re.findall(pattern, text)
    fullGram = defaultdict(int)
    common = []
    for i in range(len(full) - number):
        tup = []
        for x in range(number):
            tup.append(full[i+x])
        
        fullGram[str(tup)] +=1
        if fullGram[str(tup)] > count:
            count = fullGram[str(tup)]
            temp = tup
    """ for key in fullGram:
        print(key[1:-1],':', fullGram[key]) """
    print("Most common", number,"-gram:", temp)


def main():
    num = input("Enter N-Gram size: ")
    ngram(int(num))
    #text = 'Helo, Dave Helo, Dave. Helo, Dave Are you having a goode day?\nairth. '


if __name__ == "__main__":
    main()