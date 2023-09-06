# Solution 1 (내 풀이)
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        def dfs(elements, i) :
            
            result.append(elements[:])
            
            if len(elements) == len(nums) :
                return 
            
            for i in range(i, len(nums)) :
                elements.append(nums[i])
                dfs(elements, i+1)
                elements.pop()
   
            
        result = []
        dfs([], 0)
        return result 


# 풀이 : 39번 문제와 비슷한 풀이법으로 다른 점은 dfs를 모든 깊이로 다 방문 한다는 것이다 .
# Tip ! dfs(elements + nums[i], i) 로 호출하면 elements 리스트에 append()와 pop() 할 필요없다!!


# Solution 2 (책 풀이)
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        result = []

        def dfs(path, index) :
            # 매번 결과 추가 
            result.append(path)
            
            for i in range(index, len(nums)) :
                dfs(path + [nums[i]], i+1)
 
        dfs([], 0)
        return result 

# 풀이 : 내 풀이와 비슷하지만 , dfs(path + [nums[i]] ... 로 호출함으로써, path.append/pop() 코드 작성 필요가 없고 종료조건을 명시할 필요가 없다! 꼭 기억해두자
