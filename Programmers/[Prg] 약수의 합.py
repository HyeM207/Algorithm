# 문제 - lv.1
'''
# #1-230217 성공
    정확성: 100.0
    합계: 100.0 / 100.0
    풀이 : n//2+1만큼 for문을 돌려 그 구간안에 있는 약수를 구한다.
'''
def solution(n):
    answer = 0
    divisor = []
    
    if n in (0,1):
        return n
    
    for i in range(1, n//2 + 1) :
        if n % i == 0:
            divisor.append(n//i)
            divisor.append(i)
            
    return sum(set(divisor))


'''
(더 나은 풀이) 
    - 내 풀이 문제점 : 굳이 n//i와 i를 같이 append하여 set으로 바꾸는 등 코드 이중 작업을 했다.
    그럴 필요 없이 아래와 같이 코드를 수정하면 더 효율적인 코드가 된다.
    #2- 230217
    def solution(n):
        answer = 0
        divisor = []

        for i in range(1, n//2 +1) :
            if n % i == 0:
                divisor.append(i)
                
        return sum((divisor)) + n
'''