# 문제 - lv.1
'''
# #1-230217 성공
    정확성: 100.0
    합계: 100.0 / 100.0
    풀이  : for으로 하나씩 접근하고, 단어의 인덱스 번호를 저장하는 idx 변수를 이용하여 짝/홀수번째를 구분한다.
'''
def solution(s):
    answer = ""
    idx = 1
    for c in s : 
        if c == " ":
            idx = 1
            answer += c
        else :
            tmp = c.upper() if idx%2==1 else c.lower()
            answer += tmp
            idx += 1
            
    return answer