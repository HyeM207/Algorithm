class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        생각한 방법들 
        1. 딕셔너리로 mapping -> 순회 필요
        2. 문자열 sort로 바로 비교
        """
        return sorted(s) == sorted(t)