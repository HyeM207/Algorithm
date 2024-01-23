# 풀이 1 (240123) : 성공
from collections import deque
import copy

def solution(n, wires):
    """
    1. 그래프로 만들기
    2. 간선 하나씩 자르고
        3. 탐색하여 각 전력망 별 송전탑 개수 확인함
    """
    def bfs(graph, node, visited):
        queue = deque([node])
        cnt = 0
        
        while queue:
            v = queue.popleft()
            visited[v] = True
            cnt += 1
            for next_v in graph.get(v, []):
                if visited[next_v] == False:
                    queue.append(next_v)
                    
        return cnt, visited
    
    ###### 
    # 1. 그래프로 만들기
    answer = float('inf')
    graph = {}
    for w1, w2 in wires:
        graph[w1] = graph.get(w1, []) + [w2]
        graph[w2] = graph.get(w2, []) + [w1]

    # 2. 간선 하나씩 끊기
    for w1, w2 in wires:
        new_graph = copy.deepcopy(graph)
        new_graph[w1].remove(w2)
        new_graph[w2].remove(w1)
    
        # 3. 그래프 탐색
        visited = [False]*(n+1)
        nodes = []
        
        for node in range(1, n+1):
            if visited[node] == False:
                cnt, visited = bfs(new_graph, node, visited)
                nodes.append(cnt)
                
        if len(nodes) == 2:
            answer = min(answer, abs(nodes[0]-nodes[1]))
    
    return -1 if answer == float('inf') else answer
