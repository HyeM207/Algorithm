class Solution:
    # 풀이 1: find()함수 이용
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)