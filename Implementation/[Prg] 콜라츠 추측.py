# 문제 - lv.1
'''
# #1-230218 성공
    정확성: 100.0
    합계: 100.0 / 100.0
    풀이 : while 무한 루프를 이용해 짝/홀수 계산을 해주었다.
'''
def solution(num):
    try_cnt = 0
    
    while True:
        if num == 1 or try_cnt >= 500:
            break
        
        try_cnt += 1
        
        if num % 2 == 0 :
            num = num // 2
        else : 
            num = num *3 + 1
        
    return try_cnt if try_cnt < 500 else -1

'''
더 나은 풀이 : whlie True가 아닌 while try_cnt>=500 과 같이 조건문을 추가하는 것이 코드줄수를 줄일 수 있을 것 같다.
'''