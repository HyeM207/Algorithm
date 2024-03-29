# 풀이1 (240115) : 성공
def solution(s):
    answer = True
    
    stack = []
    for c in s:
        if c == '(':
            stack.append(c)
        else:
            if stack:
                stack.pop()
            else:
                return False

    return False if stack else True
