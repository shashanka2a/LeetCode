"""
Given an array having both positive and negative integers. The task is to compute the length of the largest subarray with sum 0.
Input:
N = 8
A[] = {15,-2,2,-8,1,7,10,23}
Output: 5
Explanation: The largest subarray with
sum 0 will be -2 2 -8 1 7.
"""

def maxLen(n, arr):
    d = {}
    s = 0
    res = 0
    for i in range(n):
        s += arr[i]
        if s == 0:
            res = i+1
        else:
            if s in d:
                res = max(res,i-d[s])
            else:    
                d[s] = i
    return res
            
