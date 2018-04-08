# checks if string is balanced with opening and closing brackets

def balance_bracket(string):
    open_bracket= string.count('[')
    close_bracket = string.count(']')
    if (open_bracket == close_bracket):
        print True
    else:
        print False