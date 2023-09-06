## 문제 - lv.1
'''
# #1-230219 성공
    정확성: 75.0
    효율성: 25.0
    합계: 100.0 / 100.0
    설명 : 에라토스테네스의 체를 이용하여 풀이함 
        [ 에라토스테네스의 체란? ]
        - 여러개의 수가 소수인지 아닌지 판별할 때 쓰는 알고리즘으로, n의 범위가 1,000,000 이하일 때 사용한다.
        - 알고리즘 : 2부터 n까지의 자연수 나열 -> 가장 작은 수의 배수를 제거함 -> 이 과정을 반복할 수 없을때까지 계속 함             
        - 참고 : https://velog.io/@changhee09/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EC%86%8C%EC%88%98%EC%9D%98-%ED%8C%90%EB%B3%84-%EC%97%90%EB%9D%BC%ED%86%A0%EC%8A%A4%ED%85%8C%EB%84%A4%EC%8A%A4%EC%9D%98-%EC%B2%B4
'''

import math 

def solution(n):
    # 에라토스테네스의 체 알고리즘 이용함
    array = [ True for i in range(n+1)]
    for i in range(2, int(math.sqrt(n))+1) : # 2부터 n의 제곱근까지만 확인하면됨
        if array[i] == True : # 남은 수(소수)인 경우
            j = 2
            while i*j <= n: # 소수의 배수들 지워나가기
                array[i*j] = False
                j += 1
    
    # 소수 개수 카운트 
    answer = 0
    for i in range(2,n+1):
        if array[i] == True:
            answer += 1
    
    return answer



'''
# 더 나은 풀이 (programmers 다른 사람 풀이 참고) : range()를 이용하여 배수들을 한번 계산 후, 배수들의 집합인 set()을 제거함   
def solution(n):
    array=set(range(2,n+1)) 

    for i in range(2, int(n**0.5)+1): # 2부터 n의 제곱근까지만 확인
        if i in array:
            num-=set(range(2*i,n+1,i)) # 배수들을 제거함
    return len(num)
'''