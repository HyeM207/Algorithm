import sys
input = sys.stdin.readline
n = int(input())
graph = []

for _ in range(n):
    graph.append(list(input().rstrip()))

print(graph)


def bfs(start_v):
    discovered = [start_v]
    queue = [start_v]
    while queue:
        v = queue.pop(0)
        for w in graph[v[0]][v[1]]:
            if w not in discovered:
                discovered.append(w)
                queue.append(w)
    return discovered

for i in range(n):
    for j in range(n):
        if graph[i][j] == '1':
            bfs([i,j])