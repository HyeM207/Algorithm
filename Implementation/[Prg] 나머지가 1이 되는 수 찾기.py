## 문제 - lv.1
'''
# #1-230319 성공
    정확성: 100.0
    합계: 100.0 / 100.0
    설명 : 약수 구하는 문제 응용편
'''

def solution(n):
    # n = 어떤수*x + 1 이므로 n-1 = 어떤수*x 임을 이용한다. 
    # n-1한 수의 약수 중 가장 작은 수를 구한다.
    n -= 1
    divisor = []
    for i in range(1, n//2+1) : 
        if n%i == 0 :
            divisor.append(i)
            divisor.append(n//i)

    return min(divisor[1:]) # 1제외하고 최소값