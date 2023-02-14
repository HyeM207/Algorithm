# 문제 - lv.1
'''
# #1-230214 성공
    정확성: 100.0
    합계: 100.0 / 100.0
    풀이 : join과 sorted 함수를 써서 손쉽게 풀었다.
'''
def solution(s):
    return ''.join(sorted(s, reverse=True))