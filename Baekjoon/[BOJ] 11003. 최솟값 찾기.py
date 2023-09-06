# 문제 : 주어진 슬라이딩 윈도우에서 최솟값 구하는 문제
# 처음에 문제 이해하기 어려웠음. 간단하게 설명하면 크기가 L인 슬라이딩 윈도우안에서 최소값 찾는 걸로 생각하면 됨
#        단 범위는 A^(i-L+1) ~ A^i 이고, 만약 A^n이 없다면 이는 무시하면 됨

# 책 풀이 (백준에는 제출 안 함)
# 관점 1: 슬라이딩 윈도우 안의 원소들을 작은 순으로 위치시켜놔야 복잡도 줄일 수 있음 -> deque 이용하기  
from collections import deque

n, L = map(int, input().split())
now = list(map(int, input().split()))

mydeque = deque () # (숫자, 인덱스) 형태의 노드 저장됨 

for i in range(n):
    while mydeque and mydeque[-1][0] > now[i]: # 덱에 들어있는 수가 현재 노드보다 크다면 덱에서 제거한다. -> 정렬 효과 
        mydeque.pop()
    
    mydeque.add( (now[i],i))

    if mydeque[0][1] <= i - L :
        mydeque.popleft()
    print(mydeque[0][0], end='') # 첫 번째 데이터 출력

# 풀이 : 덱에 (숫자, 인덱스) 형태로 저장하여 정해진 슬라이딩 윈도우 범위 내에 최소 값들을 관리한다. 