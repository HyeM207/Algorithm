class Solution:
    """
    목표 : DP를 활용하자
    2, 7, 9, 3, 1 ->  2 9 1
    2, 7, 9, 11, 5, 1 ->  2 11 1 (14) 2 9 5 (16) 
    len(nums)만큼의 배열에 각 인덱스에 최대 금액을 저장하여 그 뒤 계산을 이어가자
    """
    def rob(self, nums: List[int]) -> int:
        max_money = [0] * len(nums) 
        
        for idx, n in enumerate(nums):
            if idx-2 < 0 :
                max_money[idx] = n
                continue
            max_money[idx] = max(max_money[:idx-1]) + n
        
        return max(max_money)