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

'''
# #2-230428 성공
    풀이 : 파이썬 라이브러리 permutations 사용
    (Permutation 문제 복습 중)
'''
from itertools import permutations
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return permutations(nums)
    
'''
# #3-230428 성공
    풀이 : 파이썬 라이브러리 permutations 사용
    (Permutation 문제 복습 중)
    로직 -> nums = [1,2,3]
    dfs ([1,2,3]) -> dfs([2,3]) -> dfs([2]) 혹은 dfs([3]) -> dfs() 되어 순열 prev_elements가 완성됨
                -> dsf([1,3]) -> dfs([1]) 혹은 dfs([3]) -> dfs() 되어 순열 prev_elements가 완성됨
                ->  dsf([1,2]) -> dfs([1]) 혹은 dfs([2]) -> dfs() 되어 순열 prev_elements가 완성됨
'''
from itertools import permutations
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        results = []
        prev_elements = [] # 사용한 원소들이 쌓여서 순열 형성함

        def dfs(elements) :
            if len(elements) == 0 : # 리프 노드일 경우 return
                results.append(prev_elements[:])
            
            for e in elements:
                # 남은 원소들
                next_elements = elements[:] # 깊은 복사가 핵심!
                next_elements.remove(e) 
                
                # 사용한 원소 순열에 저장 후 dfs재귀 호출로 다음 원소 붙이기 
                prev_elements.append(e)
                dfs(next_elements[:])
                prev_elements.pop()

        dfs(nums)
        return results                
        