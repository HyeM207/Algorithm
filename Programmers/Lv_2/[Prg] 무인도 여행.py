import sys
limit_number = 10000
sys.setrecursionlimit(limit_number)

def solution(mapss):
    def dfs(i, j):
        if i < 0 or i >= height or j < 0 or j >= width or visited[i][j] or maps[i][j] == 'X':
            return 0
        
        visited[i][j] = True
        hap = int(maps[i][j])
        hap += dfs(i - 1, j)
        hap += dfs(i + 1, j)
        hap += dfs(i, j - 1)
        hap += dfs(i, j + 1)
        return hap

    maps = mapss
    width = len(maps[0])
    height = len(maps)
    visited = [[False] * width for _ in range(height)] #원래보다 한 칸씩 늘림
    result = []

    for i in range(height):
        for j in range(width):
            if maps[i][j] != 'X' and not visited[i][j]:
                hap = dfs(i, j)
                if hap != 0:
                    result.append(hap)

    result.sort()
    return result if result else [-1]
