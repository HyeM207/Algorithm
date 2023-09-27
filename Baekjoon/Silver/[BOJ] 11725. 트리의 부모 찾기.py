# 실버2
import sys
sys.setrecursionlimit(10**7)

n = int(input())
graph = {}

for i in range(n-1):
    a, b = map(int, input().split())
    graph[a] = graph.get(a, []) + [b]
    graph[b] = graph.get(b, []) + [a]

answer = [-1] * (n+1) # 2번 노드부터 n번 노드까지 
visited = [False] * (n+1) # 1번 노드 => 인덱스 1

def dfs(node):
    if visited[node]:
        return
    visited[node] = True
    for n in graph[node]:
        if answer[n] == -1:
            answer[n] = node
        dfs(n)
    
dfs(1)
print('\n'.join(map(str,answer[2:])))