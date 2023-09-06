# Solution 1
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
         
        def dfs(i,j) :
            # 이동할 수 있는 대륙(1)이라면 해당 땅으로 이동하고, 확인했다는 의미로 '1' -> '0'으로 바꿔준다.
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[i]) or grid[i][j] != '1' :
                return 
            
            grid[i][j] = '0'
            
            # 동서남북으로 이동
            dfs(i-1, j)
            dfs(i+1, j)
            dfs(i, j+1)
            dfs(i, j-1)
            
        count = 0    
        for i in range(len(grid)) : 
            for j in range(len(grid[i])) : 
                if grid[i][j] == '1':                      
                    count += 1
                    dfs(i,j)
                    
        return count
                    

# 풀이 : dfs를 이용한 문제로, main에서는 주어진 리스트를 이동하다가 1(대륙)이 나오면 dfs함수를 호출하여 섬을 돌아다닌다. 
# 섬을 '동서남북' 방향으로 돌아다니고, 들린 땅은 '0' 으로 바꿔준다. 그리고 만약 섬을 다 돌았다면, dfs 함수를 탈출한다. 