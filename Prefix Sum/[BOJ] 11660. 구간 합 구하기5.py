# 시도 1 (실패) - 시간 초과 
# 방법 : 중첩 for문

# import sys
# input = sys.stdin.readline

# n, m = map(int, input().split())
# sum = 0
# nList = []

# # 표 입력받기
# for _ in range(n) :
#     row = list(map(int, input().split()))
#     nList.append(row)

# # 입력받고 출력하기
# for _ in range(m):
#     sum = 0
#     rangeList = list(map(int, input().split()))
#     for i in range(rangeList[0]-1, rangeList[2]) :
#         for j in range(rangeList[1]-1, rangeList[3]) :
#             sum += nList[i][j]

#     print(sum)

################################################################
# 시도 2 (성공) - 책 참고
# 방법 : 부분합

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nTable = [[0] * (n+1)]
subSum = [[0] * (n+1) for _ in range(n+1)]


# 표 입력받기
for _ in range(n) :
    row = [0] + [int(x) for x in input().split()]
    nTable.append(row)

# 부분합 구하기
for i in range(1, n+1):
    for j in range(1, n+1):
        subSum[i][j] = subSum[i][j-1] + subSum[i-1][j] - subSum[i-1][j-1] + nTable[i][j] # subSum[x][y] 는 [0][0] ~ [i][j] 까지의 사각형안의 수들 합 

# 입력받고 출력하기
for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    result = subSum[x2][y2] - subSum[x1-1][y2] - subSum[x2][y1-1] + subSum[x1-1][y1-1] # 왼쪽과 오른쪽 여백 부분을 제외하고, 제외한 것의 중복된 수를 더한다 
    print(result)

