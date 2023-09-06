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
##############################
# 시도 2 - 230109 풀이 (실패_시간초과)
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
nList = list(map(int, input().split()))

prefix_sum = [0]
temp = 0

# 부분 합 배열 채우기
for i in nList :
    temp += i
    prefix_sum.append(temp)

dap = 0

# 모든 구간 확인하며 나머지 계산
for x in range(n-1):
    for y in range(x, n):
        print(x,y)
        left = (prefix_sum[y]-prefix_sum[x])//3
        if left == 0 : 
            dap += 1

print(dap)
'''
! 리뷰 ! 
연산이 2번 반복되어 시간초과 걸렸다. 
이를 개선하기 위해서는 위의 책 풀이처럼 구간 합 배열 저장 시 미리 나머지 연산까지 수행해서 저장한다. 
정답을 위해 카운트 해야하는 것은 총 3가지 이다.
    1. 원소 값이 0인 원소의 개수를 카운트
        - 0인 것은 나누어 떨어진다는 의미
    2. 나머지 값이 같은 합 배열의 개수를 카운트
        - S[i]%M과 S[j]%M이 같다면, (S[i]-S[j])%M은 0이다.
    3. 원소 값이 같은 2개의 원소를 뽑는 모든 경우의 수
 '''