"""
Given an array of integers A and an integer B.

Find the total number of subarrays having bitwise XOR of all elements equals to B.

Problem Constraints

1 <= length of the array <= 105
1 <= A[i], B <= 109
"""

def solve(self, A, B):
    d = {}
    c,x = 0,0
    for i in range(len(A)):
        x = x^A[i]
        if x^B in d:
            c+=d[x^B]
        if x==B:
            c+=1
        if x in d:
            d[x] = d[x]+1
        else:
            d[x] = 1
    return c
