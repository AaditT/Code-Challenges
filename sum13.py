# Return the sum of the numbers in the array, returning 0 for an empty array. Except the number 13 
# is very unlucky, so it does not count and numbers that come immediately after a 13 also do not count.

def sum13(list):
    has13 = False
    if (len(list) == 0):
        print 0
    else:
        for number in list:
            if (number == 13):
                has13 = True
    if (has13):
        new_list = []
        val = list.index(13)
        counter = 0
        while (counter < val):
            new_list.append(list[counter])
            counter = counter + 1
        print new_list