# Return the sum of the numbers in the array, except ignore sections of numbers 
# starting with a 6 and extending to the next 9 (every 6 will be followed by at least one 7)
# Return 0 for no numbers.

def summer_69 (list):
    six_nine = False
    _six = 0
    _nine = 0
    sum = 0
    if len(list) == 0:
        return 0
    else:
        counter = 0
        for number in list:
            sum = sum + number
            if (number == 6):
                six_nine = True
                _six = list.index(number)
            if (number == 9):
                six_nine = True
                _nine = list.index(number)
            counter = counter + number
        if (six_nine == True):
            for x in range (_six, _nine+1):
                sum = sum - list[x]
        print sum