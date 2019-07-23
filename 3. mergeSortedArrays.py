def mergeSortedArrays(array1, array2):
    if len(array1) == 0:
        return array2
    if len(array2) == 0:
        return array1

    newArray = []

    array1Counter = 0
    array1Item = array1[array1Counter]

    array2Counter = 0
    array2Item = array2[array2Counter]

    while True:
        if array1Item < array2Item:
            newArray.append(array1Item)
            array1Counter += 1
            if array1Counter >= len(array1):
                newArray += array2[array2Counter:]
                return newArray
            array1Item = array1[array1Counter]
        else:
            newArray.append(array2Item)
            array2Counter += 1
            if array2Counter >= len(array2):
                newArray += array1[array1Counter:]
                return newArray
            array2Item = array2[array2Counter]

# O (n)

print(mergeSortedArrays([2,10,50,100], [1,5,7,11,30]))
print(mergeSortedArrays([1,2,3,4], [1,5,7,11,30]))
print(mergeSortedArrays([], [-1, 1,5,7,11,30]))
