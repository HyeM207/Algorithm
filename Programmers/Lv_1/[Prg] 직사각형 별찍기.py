## 문제 - lv.1
'''
# #1-230218 성공
    정확성: 100.0
    합계: 100.0 / 100.0
    설명 : for문으로 행을, 문자열 곱셈으로 열을 출력함
'''
a, b = map(int, input().strip().split(' '))
for _ in range(b) :
    print(a*"*")


'''
# 더 나은 풀이 (programmers 다른 사람 풀이 참고) : 아래와 같이 모두 행과 열을 문자열 곱셈으로 출력가능하다.
    answer = ('*'*a +'\n')*b
    print(answer)
'''