class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        나누기 없이 진행이라..
        - hint 1: 왼쪽과 오른쪽 곱 배열 
                nums = [1,2,3,4]
                    left   1 1 2 6
                    right 24 12 4 1
        """
        len_n = len(nums) # 4
        answer = [1] * len_n
        
        left_multi = 1
        right_multi = 1
        for i in range(len_n):
            # 왼쪽 곱셈
            if i != 0:
                left_multi *= nums[i-1]
            answer[i] *= left_multi
            # 오른쪽 곱셈
            if i != 0:
                right_multi *= nums[len_n-i]
            answer[len_n-i-1] *= right_multi
        
        return answer