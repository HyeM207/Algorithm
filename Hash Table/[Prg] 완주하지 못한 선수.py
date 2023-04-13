# 문제 - lv1
'''
# #1_230206 성공 
    정확성: 58.3
    효율성: 41.7
    합계: 100.0 / 100.0
    : 스택/큐로 풀이
'''
def solution(p, c):
    p.sort()
    c.sort()
    
    flag = True

    while c: 
        tmp = p.pop()
        
        if tmp != c.pop() : 
            flag = False
            return tmp
        
    if flag : 
        return p.pop()

'''
# #2_230206 성공 
    정확성: 58.3
    효율성: 41.7
    합계: 100.0 / 100.0
    : (풀이참고) collections의 Counter 이용한 간단히 풀이
'''
import collections 

def solution(part, comp):

    result = collections.Counter(part) - collections.Counter(comp)
    return list(result.keys())[0]

'''
# #3_230413 성공 
    정확성: 50.0
    효율성: 50.0
    합계: 100.0 / 100.0
    : 해시 구조인 딕셔너리를 이용한 정석 풀이
'''
def solution(participant, completion):
    part_dict = {}
    answer = ''
    for p in participant:
        part_dict[p] = part_dict.get(p,0) + 1
    for c in completion : 
        part_dict[c] -= 1 
    
    for k, v in part_dict.items() :
        if v != 0 : 
            answer = k
    return answer