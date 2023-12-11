class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        풀이 1. set으로 중복 제거 O(n) -> sort로 정렬 O(nlogn) -> 연속인지 for문 돌며 확인 O(n)
            => O(nlogn)
        """
        if len(nums) < 2:
            return len(nums)
        
        nums = list(set(nums))
        nums.sort()
        answer = 1
        cnt_seq = 1
        
        for i in range(1, len(nums)): 
            if nums[i-1] + 1 == nums[i]:
                cnt_seq += 1
            else:
                answer = max(answer, cnt_seq)
                cnt_seq = 1
        answer = max(answer, cnt_seq)
        return answer
        