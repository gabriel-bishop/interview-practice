def reverseString(aString):
    return aString[::-1]


def reverseString2(aString):
    newString = ""


    # add to the front of the string
    for char in aString:
        newString = char + newString
        
    return newString


print(reverseString("hello"))
print(reverseString2("hello"))

# O(n)
