"""
Count the number of prime numbers less than a non-negative number, n.

Example:

Input: 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
"""




def countPrimes(self, n):
    if n<2:
        return 0
    prime = [1]*(n+1)
    prime[0],prime[1] = 0,0
    p = 2
    while (p * p <= n): 
        if (prime[p] == 1): 
            for i in range(p * p, n+1, p): 
                prime[i] = 0
        p += 1
    return sum(prime)-prime[n]
