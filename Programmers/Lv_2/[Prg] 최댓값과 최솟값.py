# 풀이 1 (240115) : 성공
def solution(s):
    l = list(map(int, s.split()))
    return  f"{min(l)} {max(l)}"
