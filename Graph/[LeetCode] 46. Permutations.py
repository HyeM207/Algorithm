# Solution 1 
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        def dfs (elements)  :
            
            if len(elements) == len(nums) :
                result.append(elements[:])   
                return
            
            next_elements = nums[:]
            # elements는 이전에 썼던 요소 저장 
            for e in elements:
                next_elements.remove(e)
            

            for e in next_elements : 
                elements.append(e)
                dfs(elements)
                elements.pop()
                    
                    
        if nums == [] :
            return []
        
        result = []
        dfs([])  
        
        
        return result

# 풀이 : dfs를 이용하는데, element는 이전에 사용한 요소들을 저장한 리스트로, 추가되는 값은 이전에 사용한 요소(elements)를 제거한 값이 저장된다.

