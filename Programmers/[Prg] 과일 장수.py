## 문제 - lv.1
'''
# #1-230319 성공
    정확성: 100.0
    합계: 100.0 / 100.0
    설명 : reverse 정렬을 하여 사과 상자에 들어가는 개수만큼 for문을 돌려가며 한 상자의 이익을 계산하여 더하였다.
'''
def solution(k, m, score):
    answer = 0
    score.sort(reverse=True)

    for i in range(0,len(score),m) :
        if i + m <= len(score) :
            answer += score[i+m-1] * m
            
    return answer