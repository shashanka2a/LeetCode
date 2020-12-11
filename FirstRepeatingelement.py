"""
Given an integer array A of size N, find the first repeating element in it.

We need to find the element that occurs more than once and whose index of first occurrence is smallest.

If there is no repeating element, return -1.

Problem Constraints
1 <= N <= 105
1 <= A[i] <= 109


Input Format
First and only argument is an integer array A of size N.

Output Format
Return an integer denoting the first repeating element.

Example Input
Input 1:

A = [10, 5, 3, 4, 3, 5, 6]

Input 2:

A = [6, 10, 5, 4, 9, 120]


Example Output
Output 1:
5

Output 2:
-1
"""

def solve(self, A):
    d = {}
    for i in range(len(A)):
        if A[i] not in d:
            d[A[i]] = [1,i] 
        else:
            d[A[i]][0] += 1 
            d[A[i]][1] = min(i,d[A[i]][1])
    #print(d)
    l = list(d.values())
    l.sort(key = lambda x:x[1])
    mn = int(1e6)
    for x in l:
        if x[0]>1:
            mn = min(x[1],mn)
    for i in range(len(A)):
        if d[A[i]][0]>1 and d[A[i]][1]==mn:
            return A[i]
    return -1
