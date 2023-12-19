# 231219 성공
# 풀이 1 (실패): 모든 경우의 수 => 시간 초과 
import sys

def solution(x, y, n):
    def calculate(t, cnt):
        if t == y:
            return cnt
        if t > y:
            return -1
    
        answer = float('inf')
        a = calculate(t + n, cnt + 1)
        if a != -1:
            answer = a
        b = calculate(t * 2, cnt + 1)
        if b != -1:
            answer = min(answer, b)
        c = calculate(t * 3, cnt + 1)
        if c != -1:
            answer = min(answer, c)
        
        return answer if answer != float('inf') else -1
        
    return calculate(x, 0)


# 풀이 2 (성공): dp => O((y-x+1)*n)
def solution(x, y, n):
    dp = [-1] * (y-x+1) # dp[i]는 x+i가 되기 위한 최소 연산 횟수
    dp[0] = 0
    
    for i in range(len(dp)):
        if dp[i] != -1:
            # 총 3번의 연산 실행 (y보다 작을때만 저장)
            t = i+x
            if t*2 <= y:
                dp[t*2-x] = min(dp[i]+1, dp[t*2-x]) if dp[t*2-x] != -1 else dp[i]+1
            if t*3 <= y:
                dp[t*3-x] = min(dp[i]+1, dp[t*3-x]) if dp[t*3-x] != -1 else dp[i]+1
            if t+n <= y:
                dp[t+n-x] = min(dp[i]+1, dp[t+n-x]) if dp[t+n-x] != -1  else dp[i]+1

    return dp[-1]

# 풀이 3 (다른 풀이 참고) : set을 이용하여 계산한 값들을 저장 및 갱신함
def solution(x, y, n):
    answer = 0
    s = set()
    s.add(x)

    while s:
        if y in s:
            return answer

        nxt = set()
        for i in s:
            if i+n <= y:
                nxt.add(i+n)
            if i*2 <= y:
                nxt.add(i*2)
            if i*3 <= y:
                nxt.add(i*3)
        s = nxt
        answer+=1

    return -1
