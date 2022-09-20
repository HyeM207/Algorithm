# 책 풀이 참고
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nList = list(map(int, input().split()))

subSum = [0] * n
remainders = [0] * m
subSum[0] = nList[0]
answer = 0

# 합 배열 저장 
for i in range(1, n):
    subSum[i] = subSum[i-1] + nList[i]

# 나머지 계산
for i in range(n):
    remainder = subSum[i] % m 
    if remainder == 0:
        answer += 1
    remainders[remainder] += 1

# 구간 개수 카운트
for i in range(m):
    if remainders[i] > 1:
        answer += (remainders[i] * (remainders[i] -1) // 2) 

print(answer)