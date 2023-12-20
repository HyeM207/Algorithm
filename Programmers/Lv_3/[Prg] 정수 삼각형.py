# 231220 성공
# 풀이 1: dp 2차원 배열로 누적합 이용한 풀이 => O(n^2)
def solution1(triangle):
    """
    j인덱스는 아래층으로 내려가면 j 또는 j+1인덱스 칸으로만 감
    풀이 : 똑같은 배열을 만들어서, 해당 배열에는 해당 칸까지의 최대 누적합을 저장한다. 
    """
    dp = [[0] * i for i in range(1, len(triangle) + 2)]
    
    for i, floor in enumerate(triangle):
        for j, n in enumerate(floor):
            dp[i + 1][j] = max(dp[i + 1][j], dp[i][j] + n)
            dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j] + n)  

    return max(dp[-1])

# 풀이 2: dp 1차원 배열로 누적합 이용한 풀이 => O(n^2)
def solution(triangle):
    height = len(triangle)
    dp = [0] * height # 맨 아래칸 기준 칸수로 누적합 담는 배열 
    
    dp[0] = triangle[0][0]
    for i in range(1, height):
        for j in range(i, -1, -1): # 꼭 역순으로 해줘야됨 
            if j == i: # 맨 오른쪽 칸
                dp[j] = dp[j - 1] + triangle[i][j]
            elif j == 0: # 맨 왼쪽 칸
                dp[j] = dp[j] + triangle[i][j]
            else: # 그 외의 칸
                dp[j] = max(dp[j - 1], dp[j]) + triangle[i][j]
              
    return max(dp)
