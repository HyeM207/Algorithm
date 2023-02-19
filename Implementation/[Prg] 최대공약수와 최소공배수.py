## 문제 - lv.1
'''
# #1-230219 성공
    정확성: 100.0
    합계: 100.0 / 100.0
    설명 : 유클리드 호제법 풀이를 이용하여 최대공약수를 구함
        [ 유클리드 호제법 ]
        1. 입력으로 두 수 m,n(m>n)이 들어온다.
        2. n이 0이라면, m을 출력하고 알고리즘을 종료한다.
        3. m이 n으로 나누어 떨어지면, n을 출력하고 알고리즘을 종료한다.
        4. 그렇지 않으면, m을 n으로 나눈 나머지를 새롭게 m에 대입하고, m과 n을 바꾸고 3번으로 돌아온다.
        - 출처 : https://ko.wikipedia.org/wiki/%EC%9C%A0%ED%81%B4%EB%A6%AC%EB%93%9C_%ED%98%B8%EC%A0%9C%EB%B2%95
'''
# 최대공약수(gcd) : 유클리드 호제법 
def gcd(n, m) : 
    if m < n :
        m, n = n, m
    
    while n != 0 :
        r = m%n
        m, n = n, r
    return m
    

def solution(n, m):
    answer = []
    
    # 최대공약수(gcd) : 유클리드 호제법 
    answer.append(gcd(n, m))
    
    # 최소공배수(lcm) : (m*n) / gcd(m,n)
    answer.append((m*n)/answer[0])
    return answer
