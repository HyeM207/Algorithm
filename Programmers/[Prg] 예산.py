# 문제 - lv.1 
'''
# #1-230220 성공
    정확성: 100.0
    합계: 100.0 / 100.0
    풀이 : 리스트를 작은 원소부터 정렬하여, 작은 것 가격을 예산에서 빼가며, 예산을 넘지 않은 개수를 구한다.
'''
def solution(d, budget):
    answer = 0
    d.sort()

    while answer < len(d) :
        if budget - d[answer]  >= 0:
            budget -= d[answer] 
            answer += 1
        else :
            break

    return answer