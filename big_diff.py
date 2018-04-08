# returns the biggest number from a list

def biggestNum(list):
    bigNum = list[0]
    counter = 0
    while (counter < len(list)):
        if (list[counter] > bigNum):
            bigNum = list[counter]
        counter = counter + 1
    return bigNum

# returns the smallest number from a list

def smallestNum(list):
    smallNum = list[0]
    counter = len(list) - 1
    while (counter > 0):
        if (list[counter] < smallNum):
            smallNum = list[counter]
        counter = counter - 1
    return smallNum

# returns the difference of the biggest number and smallest number from a list

def big_diff(list):
    list_small = smallestNum(list)
    list_big = biggestNum(list)
    difference = list_big - list_small
    print difference