# checks if a given word is a palindrome

def palindrome(string):
    backward = len(string) - 1
    b_string = ''
    while (backward >= 0):
        b_string += string[backward]
        backward = backward - 1
    if (b_string == string):
        print True
    else:
        print False