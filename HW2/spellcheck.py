import re
import timeit

#Source: GeeksforGeeks
def editDistance(str1, str2):
    m = len(str1)
    n = len(str2)
    dp = [[0 for x in range(n + 1)] for x in range(m + 1)]
    # Fill d[][] in bottom up manner 
    for i in range(m + 1): 
        for j in range(n + 1): 
  
            # If first string is empty, only option is to 
            # insert all characters of second string 
            if i == 0: 
                dp[i][j] = j    # Min. operations = j 
  
            # If second string is empty, only option is to 
            # remove all characters of second string 
            elif j == 0: 
                dp[i][j] = i    # Min. operations = i 
  
            # If last characters are same, ignore last char 
            # and recur for remaining string 
            elif str1[i-1] == str2[j-1]: 
                dp[i][j] = dp[i-1][j-1] 
  
            # If last character are different, consider all 
            # possibilities and find minimum 
            else: 
                dp[i][j] = 1 + min(dp[i][j-1],        # Insert 
                                   dp[i-1][j],        # Remove 
                                   dp[i-1][j-1])    # Replace 
  
    return dp[m][n]

def spellChecker(input):
    filename = './mobydick.txt'
    myFile = open(filename)
    text = myFile.read()
    pattern = re.compile(r'\w+')
    full = re.findall(pattern, text)
    #list = []
    ret_dict = {}
    for mispelled in re.findall(pattern,input):
        #print(mispelled)
        list = []
        counter = 1
        if not re.search(mispelled, text):
            #print("Finding: " + mispelled)
            for moby in full:
                dist = editDistance(mispelled, moby) 
                if dist == counter:
                    #print("Found: " + moby)
                    if moby not in list:
                        list.append(moby)
                        counter = 2
                        if len(list) == 3:
                            #print("Breaking: ", len(list))
                            ret_dict[mispelled] = list
                            #print(ret_dict)
                            break
    return ret_dict

def main():
    text = 'Helo, Dave. Are you having a goode day?\nairth. I hoper everything is gon wll wth you'
    result = spellChecker(text)
    for key in result:
        temp = ''
        for items in result[key]:
            temp += str(items)
            temp += ', '
        print(key,':', temp[:-2])
    #print()

if __name__ == "__main__":
    main()