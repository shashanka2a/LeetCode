"""
You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

Example 1:

Input: coins = [1, 2, 5], amount = 11
Output: 3 
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
"""


def coinChange(self, coins: List[int], amount: int) -> int:
    dp = [float(inf)]*(amount+1)
    dp[0] = 0 
    for i in range(1,len(dp)):
        for j in coins:
            if j<=i:
                dp[i] = min(dp[i-j]+1,dp[i])
    ans = dp[-1]
    if ans==float(inf):
        return -1
    return ans
