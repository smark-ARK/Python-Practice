def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(len(nums)):
            print(i, j)
            if nums[i] + nums[j] == target and i != j:
                return [i, j]


print(twoSum([3, 2, 4], 6))

