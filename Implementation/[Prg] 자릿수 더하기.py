# 문제 -lv.1
'''
# #1-230217 성공
    정확성: 100.0
    합계: 100.0 / 100.0
    내용 : sum 함수를 이용해 한줄로 품. 너무 쉬운 문제였다.
'''
def solution(n):
    return sum(int (i) for i in list(str(n)) )