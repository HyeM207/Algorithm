# 문제 - lv.1
'''
# #1-230215 성공
    정확성: 100.0
    합계: 100.0 / 100.0
    풀이 : 문자열 합치기 +와 index() 함수 이용함
'''
def solution(seoul):
    return "김서방은 " + str(seoul.index("Kim")) + "에 있다"


'''
(programmers 풀이 참고) format을 이용하면 더 깔끔한 풀이가 가능하다
    return "김서방은 {}에 있다".format(seoul.index('Kim'))
'''

