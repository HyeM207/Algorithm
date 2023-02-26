# 문제 - lv.1
'''
# #1-230226 성공
    - 정확성: 100.0
    - 합계: 100.0 / 100.0
    - 풀이 : 문제 그래도 해석하여 코드 짜면되는 쉬운문제
'''

def solution(a, b):
    result = []
    for i, j in zip(a, b) : 
        result.append(i*j)
    return sum(result)

'''
# 더 간편한 풀이(한줄코드 - prgrammers 다른 사람 풀이 참고) : 아래와 같이 한 줄로도 코딩 가능하다.
def solution(a, b):
    return sum([x*y for x, y in zip(a,b)])
'''