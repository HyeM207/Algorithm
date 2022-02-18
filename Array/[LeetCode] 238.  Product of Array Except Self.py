# Solution 1
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        cmltv_f = 1
        cmltv_b = 1
        front = deque()
        back = deque()
        
        len_nums = len(nums)
        
        # 1. 왼쪽/오른쪽 누적 곱 계산후 deque에 저장
        for i in range(len_nums-1):
            cmltv_f *= nums[i]
            cmltv_b *= nums[len_nums - i - 1]
            
            front.append(cmltv_f)
            back.append(cmltv_b)
           
        
        # 2. 왼쪽, 오른쪽 누적 곱 저장값으로 result 배열 계산
        result = []
        
        result.append(back.pop())
        
        for i in range(len_nums-2) : 
            result.append(back.pop() * front.popleft())
            
        result.append(front.popleft())

        return result


# Solution 2
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        result = [] # 최종 결과 배열 (1차: 왼쪽 누적 값)
        cmltv = 1 # 누적 값
        
        
        # 1. 왼쪽 누적 합 저장 
        for i in range(0, len(nums)) :
            result.append(cmltv)
            cmltv *= nums[i]
        
        # 2. 왼쪽 누적 결과 값에 오른족 값 차례대로 곱셈
        cmltv = 1
        
        for i in range(len(nums)-1, -1 ,-1):
            result[i] = result[i] * cmltv
            cmltv *= nums[i]
            
        return result