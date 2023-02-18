## 문제 - lv.1
'''
# #1-230218 성공
    정확성: 100.0
    합계: 100.0 / 100.0
    설명 : 구구단문제. for문을 이용해 x의 배수 리스트를 만들었다.
'''
def solution(x, n):
    answer = []
    for i in range(1,n+1):
        answer.append(x*i)
    return answer


'''
# 더 나은 풀이 (programmers 다른 사람 풀이 참고) : for문 돌릴 때 x만큼 더하도록 옵션 지정하면 더 간단한 코드 구성이 가능하다.
    return [i for i in range(x, x*n+1, x)]
'''