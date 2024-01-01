# 풀이 1 (240101) : 성공
def solution(n):
    """ 
    DP 이용하기 : 배열 이용
    n 칸 = (n-1)칸 값 + (n-2)칸 값
    """
    dp = [0] * (n+1)
    
    dp[0] = 1 # n=0
    dp[1] = 1 # n=1
    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    
    return dp[-1] % 1234567
