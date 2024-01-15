# 풀이 1 (240116) : 성공
def solution(n):
    def search(start):
        hap = 0
        for i in range(start, n+1):
            hap += i
            if hap == n:
                return True
            if hap > n :
                break
        return False
    
    answer = 0
    for i in range(1,n+1):
        if search(i):
            answer += 1
    
    return answer
