# 문제 - lv.1 
'''
# #1-230223 성공
    정확성: 100.0
    합계: 100.0 / 100.0
    풀이 : 주어진 그대로 해석하여, 전체 금액을 구한후 그에 맞게 결과값을 return해주었다. 
'''
def solution(price, money, count):
    total = 0
    for cnt in range(1, count+1):
        total += price * cnt

    return abs(total-money) if money-total<0 else 0