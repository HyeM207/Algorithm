class Solution:
    def reverseWords(self, s: str) -> str:
        # 풀이 1: 파이썬 내장 함수 이용함
        words = s.split()
        return ' '.join(words[::-1])