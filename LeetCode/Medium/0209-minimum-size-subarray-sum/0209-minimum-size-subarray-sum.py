class Solution:
    def minSubArrayLen_(self, target: int, nums: List[int]) -> int:
        """
        풀이 1 : 투포인터 (234ms)
            - 오른쪽 포인터는 합이 target보다 작을때 이동
            - 왼쪽 포인터는 합이 target보다 커졌을 때 이동
        """
        answer = 0
        left, right = 0, 0
        hap = nums[0]
        while left <= right :
            # target 값보다 hap이 큼 => 왼쪽 포인터 이동
            if hap >= target:
                if answer == 0: # 첫 갱신 값을 위함
                    answer = right-left+1
                else:
                    answer = min(answer, right-left+1)
                hap = hap - nums[left]
                left += 1
            else:
                # hap이 target보다 작음 => 오른쪽 포인터 이동하여 배열 확장
                right += 1
                if right >= len(nums):
                    break
                hap += nums[right]
                
        return answer
    
    
    def minSubArrayLen_(self, target: int, nums: List[int]) -> int:
        """
        풀이 2 : 투포인터 (풀이 1 개선) (229ms)
        """
        left, right = 0, 0
        hap = nums[0]
        answer = float('inf')

        while left < len(nums):
            if hap >= target:
                answer = min(answer, right - left + 1)
                hap -= nums[left]
                left += 1
            else:
                right += 1
                if right == len(nums):
                    break
                hap += nums[right]

        return 0 if answer == float('inf') else answer
    
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        """
        풀이 3 : 투포인터 (다른 방식의 투포인터)
            - 오른쪽 포인터 고정 후 왼쪽 포인터 이동
        """
        left = 0 
        hap = 0  # 합은 0에서 시작
        answer = float('inf')

        for right in range(len(nums)):
            hap += nums[right]
            while hap >= target: # hap이 클 때 왼쪽 포인터를 움직여 배열을 줄여감 
                answer = min(answer, right-left+1)
                hap -= nums[left]
                left += 1
                
        return 0 if answer == float('inf') else answer