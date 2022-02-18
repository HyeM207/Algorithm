# Solution 1
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        result =[]
        
        nums.sort()        
        
        for i in range(len(nums)-2) : 
            # 중복된 값은 건너뛰기
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            # 투 포인터로 간격을 좁혀가며 합 sum 계산 
            left, right = i+1, len(nums) - 1
            
            while left < right :
                sum = nums[i] + nums[left] + nums[right]
                
                if sum > 0 :
                    right -= 1
                elif sum < 0 :
                    left += 1
                else : # sum이 0인 경우
                    result.append([nums[i], nums[left], nums[right]])
                    
                    # 양 옆으로 동일한 값이 있을 수도 있으니 skip
                    while left < right and nums[left] == nums[left + 1]:
                        left +=1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                            
                    left += 1
                    right -= 1
                    
        return result