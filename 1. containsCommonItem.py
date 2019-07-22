def lookForMatch(array1, array2):
    arrayDict1 = {}
    arrayDict2 = {}
    
    for elem in array1:
        arrayDict1[elem] = True
        

    for elem in array2:
        if arrayDict1.get(elem):
            return True

    return False

print(lookForMatch([5], [7,6,8,11,9, 1]))
