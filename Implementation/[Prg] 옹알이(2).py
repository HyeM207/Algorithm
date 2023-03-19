## 문제 - lv.1
'''
# #1-230319 성공
    정확성: 100.0
    합계: 100.0 / 100.0
    설명 : 가능한 경우를 2가지로 나누어 각각 풀이함. 경우 2는 서로 다른 문자열 조합인지 확인하는 건데 이는 'check_combi'함수를 만들어 체크함.
        check_combi함수는 문자열 슬라이스를 이용하여 발음할 수 있는지 확인하고 이전과 동일한 발음이 아닌지 확인하는 로직이다.
'''
def check_combi(combi):
    start = 0
    finish = 1
    prev = ""
    while start < len(combi) : 
        if prev!= combi[start:start+2] and combi[start:start+2] in ("ye", "ma") :
            prev = combi[start:start+2]
            start += 2
        elif prev!= combi[start:start+3] and combi[start:start+3] in ("aya", "woo") :
            prev = combi[start:start+3]
            start += 3
        else :
            return False
    return True        
            
def solution(babbling):
    answer = 0    
    for b in babbling:
        # 경우 1: 가능한 문자열 그대로 발음하기
        if b in ("aya", "ye", "woo", "ma") :
            answer += 1
        # 경우 2: 서로 다른 문자열 조합
        elif check_combi(b) :
            answer += 1
        
    return answer
'''
더 나은 풀이 (programmers 다른 풀이 참고):

def solution(babbling):
    answer = 0
    for i in babbling:
        for j in ['aya','ye','woo','ma']:
            if j*2 not in i:
                i=i.replace(j,' ')
        if len(i.strip())==0:
            answer +=1
    return answer
'''