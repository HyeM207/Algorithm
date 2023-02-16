# 문제 - lv.1
'''
# #1-230216 성공
    정확성: 100.0
    합계: 100.0 / 100.0
    풀이 : for문으로 돌려 문자열 합침
'''
def solution(n):
    answer = ""
    
    for i in range(1, n+1):
        if i % 2 == 1 : 
            answer += "수"
        else : 
            answer += "박"
    
    return answer

'''
(더 나은 풀이-programmers 다른 사람 풀이 참고) 아래와 같이 인덱스 접근하면 빠르게, 효율적으로 풀 수 있겠다.
    return "".join(["수박"[i%2] for i in range(n)])
'''