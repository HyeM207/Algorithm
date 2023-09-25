# 문제 - lv.1
'''
# #1-230218 성공
    정확성: 100.0
    합계: 100.0 / 100.0
    설명 : for문으로 하나씩 이용해 접근함
'''
def solution(phone_number):
    answer = ""
    for i in range(len(phone_number)):
        if i >= len(phone_number) - 4 :
            answer += phone_number[i]
        else :
            answer += "*"
        
    return answer

'''
# 더 나은 풀이 (programmers 다른 사람 풀이 참고) : 나는 for문을 돌려서 풀이했는데, 아래 풀이는 문자열 곱셈을 이용하여 더 효율적으로 풀이하였다.
    return "*"*(len(s)-4)+s[-4:]
'''