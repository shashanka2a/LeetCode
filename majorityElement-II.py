"""
Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

Note: The algorithm should run in linear time and in O(1) space.

Example 1:

Input: [3,2,3]
Output: [3]
Example 2:

Input: [1,1,1,3,3,2,2,2]
Output: [1,2]
"""

#Moore's Voting Algo Extention

def majorityElement(self, nums: List[int]) -> List[int]:
    res = []
    ele1,ele2 = -1,-1
    c1,c2 = 0,0
    for num in nums:    
        if(num==ele1):
            c1+=1
        elif(num==ele2):
            c2+=1
        elif(c1==0):
            ele1 = num 
            c1+=1
        elif(c2==0):
            ele2 = num
            c2+=1
        else:
            c1-=1
            c2-=1
    if(nums.count(ele1) > len(nums)//3):
        res.append(ele1)
    if(nums.count(ele2) > len(nums)//3):
        res.append(ele2)
    return res
