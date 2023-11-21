class Solution:
    # 풀이1. 내장 함수 이용한 한 줄 코드
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.split()[-1])