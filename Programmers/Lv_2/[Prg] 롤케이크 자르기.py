# 풀이 1 (240118) : 성공
def solution(topping):
    """
    풀이법:  왼쪽, 오른쪽 각각 양쪽 끝에서부터 각 위치에서의 중복된 토핑 종류 수를 구하고, 
    이를 이용하여 리스트를 순회하며 왼쪽과 오른쪽의 중복된 토핑 종류 수가 같은 경우를 찾아 총 개수를 계산함
    """
    answer = 0
    left, right = [], []
    tmp = set()
    for n in topping:
        tmp.add(n)
        left.append(len(tmp))
    tmp = set()
    for n in topping[::-1]:
        tmp.add(n)
        right.append(len(tmp))
    right = right[::-1]
    
    for i in range(len(topping)-1):
        if left[i] == right[i+1]:
            answer += 1
            
    return answer

# 풀이 2 (240118) : 성공 - 풀이 1 보다 실행속도 더 빠름
from collections import Counter

def solution(topping):
    """
    풀이법: 왼쪽은 set, 오른쪽은 Counter를 이용해 중복 제거 및 종류가짓수 확인힘
    """
    answer = 0
    left = set()
    right = Counter(topping)
    
    for n in topping:
        right[n] -= 1
        if right[n] == 0:
            right.pop(n)
        left.add(n)
        if len(left) == len(right):
            answer += 1
            
    return answer
