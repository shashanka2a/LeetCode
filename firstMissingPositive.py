"""
Given an unsorted integer array nums, find the smallest missing positive integer.

Follow up: Could you implement an algorithm that runs in O(n) time and uses constant extra space.?

Example 1:

Input: nums = [1,2,0]
Output: 3
Example 2:

Input: nums = [3,4,-1,1]
Output: 2
"""

def firstMissingPositive(self, nums: List[int]) -> int:
    for i in range(len(nums)):
        while (nums[i]>0 and nums[i]<=len(nums) and nums[i]!=nums[nums[i]-1]):
            temp = nums[i]
            nums[i] = nums[nums[i]-1]
            nums[nums[i]-1] = nums[i]
    for i in range(len(nums)):
        if nums[i]!=i+1:
            return i+1 
    return len(nums)+1
