# Solution 1
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        
        nums.sort()
        result = 0
        
        for _min in nums[::2] :
            result += _min    

        return result 
    
    '''
    규칙 : 
    - 내림차순 및 오름 차순 정렬 후 순서대로 2개씩 짝지어 min 값을 넣으면 됨 
    - 어떻게 보면 홀수번째의 합을 구하면 됨 
    '''