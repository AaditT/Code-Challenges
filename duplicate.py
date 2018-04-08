# removes duplicate elements from a list

def remove_duplicate(list):
    new_list = []
    counter = 0
    while (counter < len(list)):
        if list[counter] not in new_list:
            new_list.append(list[counter])
        counter = counter + 1
    print(new_list)