def getIndex(nums, target):
    d = {}
    for index, num in enumerate(nums):
        if target - num in d:
            return [d[target - num], index]
        d[num] = index

nums = [1,2,3,4,5]
print(getIndex(nums, 9))
