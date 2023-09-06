# 문제 - lv.1
'''
# #1-230226 성공
    - 정확성: 100.0
    - 합계: 100.0 / 100.0
    - 풀이 : 문제 그래도 해석하여 코드 짜면되는 쉬운 문제
'''

def solution(absolutes, signs):
    answer = 0
    transition = { True : 1, False : -1 }
    for idx, value in enumerate(absolutes) :
        answer += (value * transition[signs[idx]] )
    return answer
