# 문제 - lv.1
'''
# #1-230214 성공
    정확성: 100.0
    합계: 100.0 / 100.0
    풀이 : 한 줄 if문과 isdigit()과 in 기능을 써서 쉽게 풀이함
'''
def solution(s):
    return True if s.isdigit() and len(s) in (4,6) else False