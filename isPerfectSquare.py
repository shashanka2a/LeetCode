"""
Given a positive integer num, write a function which returns True if num is a perfect square else False.

Follow up: Do not use any built-in library function such as sqrt.

Example 1:

Input: num = 16
Output: true
Example 2:

Input: num = 14
Output: false
"""


def isPerfectSquare(self, num):
    """
    :type num: int
    :rtype: bool
    """
    for i in range(int(math.sqrt(num))+1):
        if i*i==num:
            return True
    return False
    
    
def isPerfectSquareFast(self, num):
    """
    :type num: int
    :rtype: bool
    """
    return (math.sqrt(num) == math.ceil(math.sqrt(num)))
