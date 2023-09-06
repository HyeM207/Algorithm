## 문제 - lv.1
'''
# #1-230219 성공
    정확성: 100.0
    합계: 100.0 / 100.0
    설명 : 라이브러리 math의 sqrt함수를 이용하여 제곱근을 구함
'''
import math

def solution(n):
    answer = 0
    sqrt = int(math.sqrt(n))
    return (sqrt+1)*(sqrt+1) if sqrt*sqrt == n else -1


'''
# 더 나은 풀이 (programmers 다른 사람 풀이 참고) : **(1/2)가 제곱근인 것을 이용하면 math 라이브러리를 import 하지 않고도 풀이 가능하다
'''