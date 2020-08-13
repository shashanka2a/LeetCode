"""
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?
"""


def uniquePaths(self, m: int, n: int) -> int:
    dp = [[1 for col in range(m)] for row in range(n)]
    for row in range(1,n):
        for col in range(1,m):
            dp[row][col] = dp[row-1][col]+dp[row][col-1]
    return dp[-1][-1]
