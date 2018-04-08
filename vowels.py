# given a word, replace each vowel with a question mark

def vowels(word):
    f_string = ''
    for letter in word:
        if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u":
            f_string += "?"
        else:
            f_string += letter
    print f_string