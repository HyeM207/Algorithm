class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        """
        풀이 1 : 투포인터
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