"""
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

Your algorithm should run in O(n) complexity.

Example:

Input: [100, 4, 200, 1, 3, 2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
"""


def longestConsecutive(self, nums: List[int]) -> int:
    s = set(nums)
    max_len = 0
    for i in range(len(nums)):
        if nums[i]-1 not in s:
            curr_num = nums[i]
            curr_max = 1
            while curr_num+1 in s:
                curr_num+=1
                curr_max+=1
            max_len = max(curr_max,max_len)
    return max_len
