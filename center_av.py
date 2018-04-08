# Return the "centered" average of an array of ints, which we'll say is the mean average of the values
# except ignoring the largest and smallest values in the array. If there are multiple copies of the 
# smallest value, ignore just one copy, and likewise for the largest value. Use int division to produce 
# the final average. You may assume that the array is length 3 or more.

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

# determines the central average of given list

def center_av(list):
    list.remove(biggestNum(list))
    list.remove(smallestNum(list))
    total_sum = 0
    for number in list:
        total_sum = total_sum + number
    final_average = total_sum/len(list)
    print(final_average)