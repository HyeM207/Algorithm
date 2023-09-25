# 문제 - lv.2
"""
1차시도: 정렬하여 작은 거끼리 묶어서 태우기 -> 실패 (반례)
2차시도: 작은것과 큰 것을 합쳐서 태우자

!!! [제한] 최대 2명 !!!
"""
def solution(people, limit):
    answer = 0
    people.sort()    
    left = 0
    right = len(people) - 1
    
    while left <= right:
        if left == right:
            answer += 1
            break
        if people[left] + people[right] <= limit:
            left += 1
        answer += 1
        right -= 1
    return answer