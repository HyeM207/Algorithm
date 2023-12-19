class Solution:
    # 풀이 1 : dp
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n # dp[i]: 배열 nums에서 인덱스 i까지의 원소를 포함하는 가장 긴 증가하는 부분 수열의 길이 
        
        for i in range(1,n):
            for j in range(0, i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j]+1)
        
        return max(dp)