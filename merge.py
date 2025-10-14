def merge_list(list1, list2):
    #First, we create a new list where we merge the two lists together
    mergedList = list1 + list2

    #then, we sort the new list using any sorting algorithm. I used bubble sort

    for i in range(len(mergedList)):
        for j in range(0, len(mergedList)-i-1):
            if mergedList[j] > mergedList[j+1]:
                mergedList[j], mergedList[j+1] = mergedList[j+1], mergedList[j] #swap    

    return mergedList
