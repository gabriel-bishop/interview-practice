def firstRecurring(array):
    values = {}

    for i in range(len(array)):
        
        if values.get(array[i]):
            return array[i]

        values[array[i]] = True

    return None


# O(n)
print(firstRecurring([1,2,3,4,5, 4, 5]))
print(firstRecurring([2,1,1,2,3,5,1,2,4]))

