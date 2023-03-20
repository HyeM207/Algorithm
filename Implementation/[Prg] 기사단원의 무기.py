# 문제 - lv.1
'''
# #1-230320 실패
    정확성: 66.7
    합계: 66.7 / 100.0
    풀이 : cnt_divisor함수로 n//2+1만큼 for문을 돌려 그 구간안에 있는 약수를 구하여 개수를 return한다
    실패원인 : 시간 초과
'''
def cnt_divisor(n):
    divisor = []
    for i in range(1, n//2+1):
        if n%i == 0 :
            divisor.append(i)
            divisor.append(n//i)
    return len(set(divisor))

def solution(number, limit, power):
    # 1부터 number까지의 총 약수의 개수를 구하고, 약수의 개수가 limit 초과이면 power로 바꿔 총 약수의 개수 합을 구하는 문제
    total = [1]
    for i in range(2, number+1) :
        cnt = cnt_divisor(i)
        if cnt > limit : 
            total.append(power)
        else : 
            total.append(cnt) 

    return sum(total)