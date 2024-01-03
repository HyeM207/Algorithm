# 풀이 1 (240103) : 성공
def split_uv(w):
    """
    단계 2 : 문자열 w를 두 "균형잡힌 괄호 문자열" u, v로 분리
    """
    d = {'(':0, ')':0 }
    for i, c in enumerate(w):
        d[c] += 1
        if i != 0 and d['('] == d[')']:
            return w[:i+1], w[i+1:]
        
    return w, ""
    
def check_alright(w):
    """
    단계 3 : 올바른 괄호 문자열인지 확인
    """
    stack = [] 
    for c in w:
        if c == '(':
            stack.append(c)
        else: # )인경우
            if stack and stack.pop() == '(':
                pass
            else:
                return False
    return True if len(stack) == 0 else False

def step4_4(u):
    """
    단계 4-4 : u의 첫 번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙임
    """
    u = u[1:-1]
    new_u = ''
    for i in range(len(u)):
        if u[i] == '(':
            new_u += ')'
        else:
            new_u += '('
    return new_u

def solution(p):
    """
    단계별로 함수를 만들고 이를 주어진 알고리즘에 따라 이어붙임
    """
    # 단계 1 : 빈 문자열 확인 및 '올바른 괄호 문자열' 확인
    if p == '':
        return ''
    if check_alright(p):
        return p
    # 단계 2 : u("균형잡힌 괄호 문자열")와 v로 분리
    u, v = split_uv(p)
    # 단계 3 : v를 단계 1부터 수행 
    if check_alright(u):
        return u + solution(v)
    # 단계 4
    new_str = "(" + solution(v) + ")" + step4_4(u)
    return new_str
