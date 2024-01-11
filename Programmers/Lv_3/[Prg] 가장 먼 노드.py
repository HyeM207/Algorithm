# 풀이 1 (240111) : 성공
from collections import deque 

def solution(n, edge):
    """
    dfs가 아닌 bfs로 접근해야된다.
        - visited를 리스트가 아닌 딕셔너리로 만들어서 조회시간 줄일것
        - visited에는 거리를 저장할 것 
        - deque에서 pop이 아닌 popleft 할것!
    """
    # 1. graph 생성
    graph = {}
    for x, y in edge:
        graph[x] = graph.get(x, []) + [y]
        graph[y] = graph.get(y, []) + [x]

    # 2. bfs 구현 : 이때 visited배열에는 0(방문안함)과 그 외 숫자(1부터 거리)를 저장
    visited = [0] * (n+1)
    q = deque([(1,0)])
    visited[1] = 1
    while q:
        v, dist = q.popleft()
        for adj_v in graph[v]:
            if visited[adj_v] == 0 :
                q.append((adj_v, dist + 1))
                visited[adj_v] = dist + 1
    
    return visited.count(max(visited))
