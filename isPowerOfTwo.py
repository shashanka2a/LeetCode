"""
Given an integer, write a function to determine if it is a power of two.

Example 1:

Input: 1
Output: true 

Example 2:

Input: 16
Output: true

"""



def isPowerOfTwo(self, n):
    if n<0:
        return False
    s = bin(n).replace('0b','')
    if s.count('1')!=1:
        return False
    return True
