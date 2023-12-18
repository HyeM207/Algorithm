class Solution:
    def coinChange_(self, coins: List[int], amount: int) -> int:
        """        
        풀이 1: dp 바텀업
        """
        dp = [-1] * (amount+1) # dp[i] : i원을 만들 때 필요한 최소 동전 개수
        dp[0] = 0
        
        for i in range(len(dp)):
            if dp[i] != -1:
                for c in coins:
                    if i+c <= amount and (dp[i + c] == -1 or dp[i + c] > dp[i] + 1):
                        dp[i+c] = dp[i] + 1
                        
        return dp[-1]
    
    def coinChange(self, coins: List[int], amount: int) -> int:
        """        
        풀이 2: dp 탑다운 (메모이제이션) => 더 효율적임
        """
        memo = {}

        def dp(amount):
            if amount == 0:
                return 0
            if amount < 0:
                return -1
            if amount in memo:
                return memo[amount]

            min_count = float('inf')
            for coin in coins:
                subproblem = dp(amount - coin) # amount에서 coin을 빼는 방식으로 
                if subproblem != -1:
                    min_count = min(min_count, subproblem + 1)

            memo[amount] = min_count if min_count != float('inf') else -1
            # print(f"memo[{amount}] : {memo[amount]}")  # 결국엔 낮은 것 부터 채우고 옴
            return memo[amount]

        result = dp(amount)
        return result