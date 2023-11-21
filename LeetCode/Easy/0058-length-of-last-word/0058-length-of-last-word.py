class Solution:
    # 풀이1. 내장 함수 이용한 한 줄 코드 <- 더 나음
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.split()[-1])
    
    # 풀이2: 인덱스 접근 
    def lengthOfLastWord(self, s: str) -> int:
        result = 0
        is_started = False
        for i in range(len(s)-1 ,-1, -1):
            if s[i] == ' ' and is_started:
                break
            if s[i] != ' ':
                result += 1
                is_started = True
        return result