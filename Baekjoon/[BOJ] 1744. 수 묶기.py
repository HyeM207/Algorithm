# 230615 성공
# 1트 : 1인 경우는 더해야함을 모르고, 음수, 양수, 0 리스트로 나눔
# 2트 : 1 리스트를 따로 빼고 0을 음수 리스트와 합함
"""
두 수로 묶은 수는 곱하고 나머지는 더하는 문제
- 음수(오름차순) : 짝수개 -> 둘이곱, 홀수 개-> 0일때만 묶기
- 양수(내림차순) : 내림차순으로 둘이 곱, 1이면 더하기, 0과는 묶지 않기 
"""
import sys
input = sys.stdin.readline
n = int(input())

negative_zero = []
positive = []
one = []
answer = 0

for _ in range(n):
    t = int(input())
    if t == 1 :
        one.append(t)
    elif t > 0 :
        positive.append(t)
    else:
        negative_zero.append(t)

# 양수 처리 
positive.sort(reverse=True)
for i in range(0, len(positive), 2):
    if i+1 < len(positive):
        answer += positive[i]*positive[i+1]
    else:
        answer += positive[i]

# 음수 처리 
negative_zero.sort()
for i in range(0, len(negative_zero), 2):
    if i+1 < len(negative_zero):
        answer += negative_zero[i]*negative_zero[i+1]

# 음수 홀수 개-> 0일때만 묶기
if len(negative_zero)%2 == 1:
    answer += negative_zero[-1]

# 1일때 처리
answer += len(one)
print(answer)
