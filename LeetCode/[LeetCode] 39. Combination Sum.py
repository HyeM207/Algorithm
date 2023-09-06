# Solution 1 (내 풀이)
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        # 파라미터 : 원소들 총 합, 원소들, 인덱스
        def dfs (hap, elements, i) :
            
            # 종료 조건 1
            if hap == target : 
                result.append(elements[:])
                return True
            
            # 종료 조건 2
            if hap > target :
                return False 
            
            # 재귀 호출 
            for i in range(i, len(candidates)):
                elements.append(candidates[i])

                # rv 값을 이용하여 값이 커지면 바로 for문을 나가 이전 함수 호출로 돌아갈 수 있도록 return 한다. 
                rv = dfs (candidates[i]+hap, elements, i)
                elements.pop()

                if rv == False: 
                    return
            

        candidates.sort()    
        result = []
        dfs(0, [], 0)
        
        return result
        
        
 # 풀이 :  DFS와 for문을 이용한 풀이로, 맨 처음에는 풀이방법이 생각나지 않았지만, elements에 들어가는 요소들을 for문 단계에 따른 트리 형식처럼 그려보았더니 풀이에 도움이 되었다.
 # 1. for문을 돌며 요소들을 더해가는데, 이때 더해가는 값은 현재 더한 원소보다는 같거나 큰 원소를 더한다. 
 # 2. 또한 원소를 추가하다가 hap이 target보다 커질때는 return False를 하여 이전 함수 호출 단계로 넘어가고, 다음 for문이 실행 되지 않도록 함수 호출 결과값 False를 참고하여 한 번 더 return 해준다.
        
        
# Solution 2 (책 풀이)       
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        # 파라미터 : (target- 지금까지의 합), 순서, 탐색경로
        def dfs(csum, index, path) : 

            # 종료 조건 1
            if csum < 0 :
                return 

            # 종료 조건 2
            if csum == 0 :
                result.append(path)
                return 

            # 자기부터 하위 원소까지의 나열 재귀 호출 
            for i in range(index, len(candidates)):
                dfs(csum - candidates[i], i, path + [candidates[i]])


        result = []
        dfs(target, 0, [])
        return result 

# 풀이 : dfs(csum, index, path) 형태로 재귀호출을 한다. sum이 아닌 csum인 부분이 내 풀이와 차이가 있다. 
# 특히 주목할 점은 for문에서 dfs를 호출할 때 내 풀이와 달리 바로 값을 적용시켜 호출하는 것을 볼 수 있다. (ex.  path + [candidates[i]])
# 이 방법은 코드를 줄일 수 있으니 기억해두면 좋을 것 같다.!