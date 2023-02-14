# 문제 - lv1
'''
# #1 - 230214 성공
    정확성: 100.0
    합계: 100.0 / 100.0
    풀이 : sorted 함수의 key와 lambda로 손쉽게 품
'''
def solution(strings, n):
    return sorted(strings, key= lambda x :(x[n], x))
