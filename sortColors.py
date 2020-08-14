"""
Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note: You are not suppose to use the library's sort function for this problem.

Example:

Input: [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
"""


def sortColors(self, nums):
    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    """

    low = 0
    high = len(nums)-1
    i = 0
    while i<=high:
        if nums[i]<1:
            nums[i],nums[low] = nums[low],nums[i]
            low+=1
            i+=1
        elif nums[i]>1:
            nums[i],nums[high] = nums[high],nums[i]
            high-=1
        else:
            i+=1
