# Given an array of integers, return indices of the two
# numbers such that they add up to a specific target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# Given nums = [2, 7, 11, 15], target = 9,

def sumTo(nums, target):
    values = {}
    for i in range(0, len(nums)):
        if values.get(target - nums[i]) != None:
            return [values.get(target - nums[i]), i]
        values[nums[i]] = i


# O(n)

print(sumTo([1,2,3,4,5], 8))
print(sumTo([1,2,3,4,5], 11))


