class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """        
        풀이 1: dp 바텀업
        """
        dp = [-1] * (amount+1)
        dp[0] = 0
        
        for i in range(len(dp)):
            if dp[i] != -1:
                for c in coins:
                    if i+c <= amount and (dp[i + c] == -1 or dp[i + c] > dp[i] + 1):
                        dp[i+c] = dp[i] + 1
                        
        return dp[-1]
            