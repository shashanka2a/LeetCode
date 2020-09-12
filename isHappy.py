"""
Write an algorithm to determine if a number n is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Return True if n is a happy number, and False if not.

Example: 

Input: 19
Output: true
Explanation: 
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
"""




def isHappy(self, n):
    """
    :type n: int
    :rtype: bool
    """
    def count(n):
        c = 0
        while n:
            c+=1
            n/=10
        return c
    def sol(n):
        if count(n)==1:
            return n
        s = 0
        while n:
            d = n%10
            s+=d**2
            n/=10
        return sol(s)
    ns  = str(n)
    dp = [False]*(10)
    for i in range(1,10):
        dp[i] = sol(i**2)==1
    return sol(n)==1 or dp[sol(n)]




def isHappy(self, n):
    """
    Because if the algorithm sees a number it has seen before, then it follows that it will 
    go on the same path and thus see it once again, creating an infinite loop. So a valid solution  
    requires that all numbers seen on the way to reducing n to 1 be unique.
    """
    seen = set()
    while n not in seen:
        seen.add(n)
        n = sum([int(x) **2 for x in str(n)])
    return n == 1
