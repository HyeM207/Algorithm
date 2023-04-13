## 문제 - lv.2
'''
# #1-230413 실패
    정확성: 45.5
    합계: 45.5 / 100.0
    틀린 테스트케이스 : 1~6
    설명 : 0~1000이하의 숫자를 비교해야된다는 점에서, 3과 32를 비교시 3이 먼저와야하니까, 3333과 3222로 바꿔서 크기 비교하는 방법을 생각해냄.
    그래서 숫자를 문자열 4자리로 바꾸고 sort 하였다. 
'''
def solution(numbers):
    numbers.sort(key = lambda x: (str(x) + (str(x)[-1] * (4-len(str(x)))))[:4], reverse=True)
    result = ''.join(str(n) for n in numbers) 
    return result if result[0] != '0' else '0'


'''
# #2-230413 성공
    정확성: 100.0
    합계: 100.0 / 100.0
    설명 : (강의 참고) numbers의 원소를 먼저 문자로 바꾸고, `(x*4)[:4]`로 숫자 네자리수로 만들어서 sort()
'''
def solution(numbers):
    numbers = [ str(n) for n in numbers]
    numbers.sort(key = lambda x: (x*4)[:4], reverse=True)
    result = ''.join(numbers) 
    return result if result[0] != '0' else '0'