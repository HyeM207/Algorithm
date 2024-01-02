# 풀이 1 (240102) : 성공 
from collections import deque

def solution(order):
    """
    문제에서 제시한 알고리즘 그대로 구현함
      - 서브컨테이너는 deque이용
      - 핵심은 container와 n의 대소비교를 통해 케이스를 나눠서 구현함
    """
    q = deque()
    container = 1
    for i, n in enumerate(order):
        if n == container:
            container += 1
        elif n < container:
            if len(q) > 0 and q[-1] == n:
                q.pop()
            else:
                return i
        else: 
            # 큰 경우 서브 컨테이너에 보관 
            for i in range(container, n):
                q.append(i)
            container = n+1

    return i+1
