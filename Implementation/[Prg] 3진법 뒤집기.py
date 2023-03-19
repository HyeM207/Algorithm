## 문제 - lv.1
'''
# #1-230319 성공
    정확성: 100.0
    합계: 100.0 / 100.0
    설명 : 진법 계산 원리를 그대로 코드로 구현함
'''

def solution(n):
    answer = 0
    array = []
    
    # 3진법 계산 (3으로 계속 나누고, 나머지는 배열에 저장)
    while n > 2 :
        n, remainder =  n//3,  n%3
        print(n, remainder)
        array.append(remainder)
    
    array.append(n)
    
    # 3진법 계산
    three_cnt = 1
    while array: 
        answer += array.pop() * three_cnt
        three_cnt *= 3
    return answer

'''
더 나은 풀이 (programmers 다른 사람 풀이 참고): 나머지를 배열이 아닌 '문자열'에 저장 후, 진법을 int 함수를 이용해 바꾼 코드이다. 기억해두자! 
def solution(n):
    tmp = ''
    while n:
        tmp += str(n % 3)
        n = n // 3

    answer = int(tmp, 3)
    return answer
'''