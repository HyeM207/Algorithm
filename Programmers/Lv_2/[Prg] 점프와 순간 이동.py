# 풀이 1 (240202) : 성공
def solution(n):
    def divide_two(p, jump=0):
        if p == 1:
            return 1
        return divide_two(p//2, jump) + p%2

    return divide_two(n)
