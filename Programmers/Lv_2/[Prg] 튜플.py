# 문제 - lv.2
'''
# #1-230504 성공
- 풀이 : 앞과 맨뒤의 {{,}}를 제거 -> "},{"로 잘라서 
'''
def solution(s):
    answer = []
    s = s[2:-2]
    tuple = sorted(s.split("},{"), key=len)
    print(tuple)
    for t in tuple :
        tmp = list(map(int,t.split(',')))
        added = list(set(tmp) - set(answer))[0]
        answer.append(added)
    
    return answer