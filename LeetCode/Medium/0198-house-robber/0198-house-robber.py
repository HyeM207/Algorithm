class Solution:
    # 풀이1. 리스트를 활용한 DP
    # 각 인덱스에 대해 직전 두 집까지의 최대 금액을 비교하여 현재 집을 털 때와 털지 않을 때 중 더 큰 값을 저장
    """
    목표 : DP를 활용하자
    2, 7, 9, 3, 1 ->  2 9 1
    2, 7, 9, 11, 5, 1 ->  2 11 1 (14) 2 9 5 (16) 
    len(nums)만큼의 배열에 각 인덱스에 최대 금액을 저장하여 그 뒤 계산을 이어가자
    """
    def rob1(self, nums: List[int]) -> int:
        max_money = [0] * len(nums) 
        
        for idx, n in enumerate(nums):
            if idx-2 < 0 :
                max_money[idx] = n
                continue
            max_money[idx] = max(max_money[:idx-1]) + n
        
        return max(max_money)
    
    # 풀이2. 재귀를 이용한 DP -> 시간초과 뜸. 재귀 함수 방법만 익혀두기
    # dp(i) = max(dp(i-1), dp(i-2)+nums[i]) 를 활용함
    # 중복 계산을 피하기 위해 메모이제이션을 활용하여 이미 계산한 값은 저장하고, 저장된 값이 있을 경우 다시 계산하지 않음
    def rob2(self, nums: List[int]) -> int:
        def dp(i):
            if i <= 0:
                return nums[0]
            elif i == 1:
                return max(nums[0], nums[1])
            else:
                mem[i] = max(dp(i-1), dp(i-2)+nums[i])
            return mem[i]
        
        mem = {}
        return dp(len(nums)-1)
    
    # 풀이3. 풀이1을 간단하고 DP스럽게 바꿈
    def rob(self, nums: List[int]) -> int:
        dp = [0 for i in range(len(nums) + 1)]
        dp[0] = 0
        dp[1] = nums[0]

        for i in range(2, len(dp)):
            dp[i] = max(dp[i - 2] + nums[i - 1], dp[i - 1])

        return dp[-1]