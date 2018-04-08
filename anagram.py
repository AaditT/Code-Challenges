# checks to see if two given words are anagrams

def anagram(word1, word2):
    a = True
    if (len(word1) == len(word2)):
        for x in word1:
            if x in word2:
                a = True
            else:
                a = False
        if (a == True):
            print True
        elif (a == False):
            print False
    else:
        print False