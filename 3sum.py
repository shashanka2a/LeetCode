"""
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""

def threeSum(self, nums: List[int]) -> List[List[int]]:
    nums.sort()
    res = []
    for i in range(len(nums)-2):
        target = -1*nums[i]
        l,r = i+1,len(nums)-1
        if i>0 and nums[i]==nums[i-1]:
            continue
        while l<r:
            if nums[l]+nums[r]==target:
                res.append([nums[i],nums[l],nums[r]])
                while l<r and nums[l]==nums[l+1]:
                    l+=1
                l+=1
                r-=1
            elif nums[l]+nums[r]<target:
                l+=1
            else:
                r-=1
    return res
