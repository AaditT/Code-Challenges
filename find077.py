# checks to see if 007 is in a list

def find077(list):
    f_007 = False
    if (len(list) < 3):
        print False
    elif (len(list) >= 3):
        counter = 0
        while (counter < len(list)):
            #print list[counter]
            if (list[counter] == 0) and (list[counter + 1] == 7) and (list[counter + 2] == 7):
                f_007 = True
            counter = counter + 1
    if (f_007 == True):
        print True
    elif (f_007 == False):
        print False