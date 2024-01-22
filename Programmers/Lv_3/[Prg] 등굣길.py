# 풀이 1 (240122) : 성공
def solution(m, n, puddles):
    """
    풀이법 : dp 
    내가 착각 한 것 : answer이 경로distance가 아닌 경로의 가짓 수임
    """
    from collections import deque

    answer = 0
    dp = [ [0]*m for _ in range(n)]
    dp[0][0] = 1

    for i in range(n):
        for j in range(m):
            if i==0 and j==0: # 시작점은 pass
                 continue
            if [j+1, i+1] in puddles: # puddles는 10개 이하
                continue
            dp[i][j] = (dp[i - 1][j] + dp[i][j - 1]) % 1000000007

    return dp[-1][-1]
