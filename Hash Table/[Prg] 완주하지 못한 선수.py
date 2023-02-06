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