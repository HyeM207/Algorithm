"""
단순 dfs, bfs 문제 
    - 책 참고
    - 단뱡향이 아닌 양방향 간선 정보 주어짐
--> 264ms
"""
import sys
input = sys.stdin.readline

n, m, v = map(int, input().split())
graph = {}

for _ in range(m):
    i, j = map(int, input().split())
    # 양방향
    if i in graph:
        graph[i].append(j)
    else:
        graph[i] = [j]
    if j in graph:
        graph[j].append(i)
    else:
        graph[j] = [i]

def dfs(v, discovered=None):
    if discovered is None:
        discovered = []
    discovered.append(v)
    if v in graph.keys():
        for w in sorted(graph[v]):
            if w not in discovered:
                discovered = dfs(w, discovered)
    return discovered

def bfs(start_v):
    discovered = [start_v]
    queue = [start_v]
    while queue:
        v = queue.pop(0)
        if v in graph.keys():
            for w in sorted(graph[v]):
                if w not in discovered:
                    discovered.append(w)
                    queue.append(w)
    return discovered

result_dfs = dfs(v)
result_bfs = bfs(v)
print(*result_dfs)
print(*result_bfs)

