# 문제 - lv.1
'''
# #1-230320 성공
    정확성: 100.0
    합계: 100.0 / 100.0
    풀이 : 문자열슬라이스를 이용하여 쉽게 풀이함
'''
def solution(t, p):
    answer = 0
    for i in range(0, len(t)-len(p)+1):
        if int(t[i:i+len(p)]) <= int(p) :
            answer +=1
    
    return answer