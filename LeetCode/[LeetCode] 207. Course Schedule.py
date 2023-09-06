# Solution 1 (내 풀이_실패!)
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        # 시작 노드, 이전 노드, 다음 노드
        def dfs(start, prev, nextN) :
         
            # 종료 조건 
            if nextN in start :
                return False
    
            # 다음 노드가 graph에 있다면 이동 
            if nextN in graph :
                for n in graph[nextN]: 
                    start.add(prev)
                    rv = dfs(start, nextN, n)
                    start.remove(prev)
                    if rv == False:
                        return False

    
        # 키 : 노드 / 값 : 카 노드에 연결된 노드 리스트(그래프) 
        graph = dict() 
      
        # dfs 호출 전,연결 구조를 딕셔너리인 graph 구조로 바꾼다.  
        for p in prerequisites :
            if p[0] in graph:
                graph[p[0]].append(p[1])
            else : 
                graph[p[0]] = [p[1]]
                
    
        # (main) 모든 노드를 기반으로 dfs를 호출함 
        for s in graph:
            for n in graph[s]: 
                rv = dfs(set([s]), s, n)
                if rv == False :
                    return False
     
        return True

# 풀이 : 주어진 그래프를 딕셔너리 형태로 바꾸어, dfs를 호출한다. 순환 구조인지 판단을 통해 true/false를 구분하는데,
#       이때 순환 구조는 다음 노드가 이전에 방문했던 노드라면 false를 리런하는 형태이다. 
# 후기 : 기본 Test Case와 추가한 테스트는 통과했지만, submit의 test 과정에서 ban당하였다... (<= 순환구조인지 판단하는 알고리즘을 완전히 잘못 작성한 것으로 보임)  
#       이 말은 즉슨 알고리즘을 잘 짜지 못했다는 뜻인데, 거의 이틀 정도 고민했는데도 해결하지 못하여 책 풀이를 참고하였다. 



# Solution 2 (책 풀이)
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        # 그래프 구성
        graph = collections.defaultdict(list) 
        for x, y in prerequisites :
            graph[x].append(y)


        traced = set() # 순환구조인지 판별 위함
        visited = set() # 방문한 노드인지 판별 위함 (효율성 극대화)

        def dfs(i) : 
            # 순환구조이면 False
            if i in traced : 
                return False

            # 이미 방문한 노드이면 True
            if i in visited : 
                return True # <- True 리턴!

            traced.add(i)

            for y in graph[i] : 
                if not dfs(y) : # <= 여기 주목!
                    return False
            # 탐색 종료 후 순환 노드 삭젲 
            traced.remove(i)
            visited.add(i)

            return True

        # (main) 순환 구조 판별 
        for x in list(graph) : # list()로 묶지 않으면, defaultdict 데이터 형이라 사이즈가 변경되었다는 에러가 뜨므로, list()로 묶어준다. 
            if not dfs(x) : 
                return False
        
        return True 

# 풀이  : dfs로 순환 구조인지 확인하는 알고리즘으로, traced 집합으로 방문한 노드인지 확인하는 것이 해당 알고리즘의 핵심이다.
#       추가적으로 코드 효율성을 위해 visited 집합을 추가하여, 이미 방문한 노드는 중복하여 방문하지 않도록 한다.

# 핵심 1 : traced, visited 집합 추가
        # 1.1 순환구조이면 False
        if i in traced : 
            return False
        # 1.2 if not dfs(y)
        for y in graph[i] : 
                if not dfs(y) : # <= 여기 주목!
                    return False

# 핵심 2 : list(graph)로 defaultdict의 복사본을 만든다. 