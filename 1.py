# https://leetcode.com/problems/two-sum/

# Brute Force
def containsDuplicate(self, nums):
    for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
    return []

# Dictionary Approach

def twoSum(self, nums, target):
        x = {} 

        for i, n in enumerate(nums):
            diff = target - n
            if diff in x:
                return [x[diff], i]
            x[n] = i