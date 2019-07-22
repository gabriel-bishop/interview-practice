def lookForMatch(array1, array2):
    arrayDict = {}
    
    for elem in array1:
        arrayDict[elem] = True
        

    for elem in array2:
        if arrayDict.get(elem):
            return True

    return False

print(lookForMatch([5], [7,6,8,11,9, 1]))
