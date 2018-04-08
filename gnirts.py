# reverses a given string

def gnirts(string):
    f_string = ''
    counter = len(string) - 1
    while (counter >= 0):
        f_string += string[counter]
        counter = counter - 1
    print f_string