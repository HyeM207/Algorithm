# 문제 - lv.1
'''
# #1-230223 성공
    정확성: 100.0
    합계: 100.0 / 100.0
    풀이 : 약수 개수를 return하는 함수를 만들어서 풀이함
'''
def cnt_divisor(num): # return : 약수 개수 
    cnt = 0 
    for i in range(1,num//2 +1):
        if num % i == 0 :
            cnt += 1    
    return cnt + 1 # 자기 자신까지

def solution(left, right):
    answer = 0
    
    for n in range(left, right+1):
        if cnt_divisor(n) %2 : # 홀수 개수면 빼고 
            answer -= n
        else : # 짝수 개수면 더한다.
            answer += n
            
    return answer

'''
# 더 나은 풀이(programmers 다른 사람 풀이 참고) : 아래 수학적 정의를 이용한 엄청 효율적인 풀이이다. 아래 개념은 기억해두자.
    # 수학적 개념 : 어떤 수의 제곱근이 정수이면 약수는 홀수개이고, 제곱근이 아니면 약수는 짝수개
    # 예를 들어 16의 약수는 (1,2,4,8,16)으로 5개(홀수)인데, 실제로 제곱근은 4로 정수이므로 약수는 홀수개이다.

    def solution(left, right):
        answer = 0
        for i in range(left,right+1):
            if int(i**0.5)==i**0.5: # 제곱근이 정수인지 판단하는 조건문  
                answer -= i
            else:
                answer += i
        return answer

'''