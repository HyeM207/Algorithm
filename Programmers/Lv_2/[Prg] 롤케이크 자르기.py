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
