# 문제 - lv.2
"""
# #1-230523 성공
    정확성: 100.0
    합계: 100.0 / 100.0
    풀이 : 모든 일수를 계산함-> Counter 뺄셈 연산 이용
"""
from collections import Counter
def solution(want, number, discount):
    answer = 0
    d = {}
    for i in range(len(want)) :
        d[want[i]]=number[i]
        
    # 1일부터 되는 막날까지
    for i in range(0, len(discount)-9):
        cnt = Counter(discount[i:i+10])
        tmp = Counter(d) - cnt
        if not tmp :
            answer += 1 
    return answer