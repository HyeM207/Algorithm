class Solution:
    # 풀이 1 : dp => O(N^2)
    def lengthOfLIS1(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n # dp[i]: 배열 nums에서 인덱스 i까지의 원소를 포함하는 가장 긴 증가하는 부분 수열의 길이 
        
        for i in range(1,n):
            for j in range(0, i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j]+1)
        
        return max(dp)
    
    
    # 풀이 2: 그리디&이진 탐색 (풀이 참고) => O(nLogn) 
    """
    sub 배열에는 
    
    bisect_left(a, x) :정렬된 a에 x를 삽입할 인덱스 리턴
        만약, x가 a에 이미 있으면 기존 항목의 앞 (왼쪽)의 위치를 반환한다.
    """
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        sub = [] # 현재까지의 가장 긴 증가하는 부분 수열 저장

        for x in nums:
            if not sub or sub[-1] < x: # 현재 값이 정렬된 sub의 가장 큰 값보다 크다면
                sub.append(x)
            else:
                 # 현재 값이 정렬된 sub의 가장 큰 값보다 작다면 값을 교체함
                i = bisect_left(sub, x)
                sub[i] = x

        return len(sub)