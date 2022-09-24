# 문제 : n개의 숫자카드를 규칙에 따라 버리다가 마지막 하나 남은 카드의 수를 구하는 문제 
# 내 풀이 - 성공 
from collections import deque

n = int(input())
mydeque = deque ()

# 원소 넣기
for i in range(n):
    mydeque.append(i+1)

# 규칙 적용
while len(mydeque) > 1:
    mydeque.popleft()
    tmp = mydeque.popleft()
    mydeque.append(tmp)

print(mydeque.popleft())

# 풀이 : deque를 이용하여 쉽게 풀이 가능함
# 개선사항 : 두 줄을 다음과 같이 한 줄로 바꾸면 더 좋을 듯 함. mydeque.append(mydeque.popleft())