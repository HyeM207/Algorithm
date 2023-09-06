# Solution 1
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        def dfs(index, path) :  # index는 추가되는 값의 시작점. path는 조합 리스트
            if index > n+1 or len(path) > k: 
                return 
            
            if len(path) == k :
                result.append(path[:])
                return
            
            for i in range(index, n+1) :  
                path.append(i)
    
                dfs(i+1, path)
                path.pop()
            
        result = []
        
        dfs(1,[])
        
        return result

# 풀이 : dfs를 이용하고, dfs는 조합 길이를 만족할때만 return 된다. 참고로 추가되는 값은 이전에 추가된 값 +1 (=i+1) 이므로, for문을 이용하여 값을 추가한다.