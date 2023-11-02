class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        생각한 방법들 
        1. 문자열 sort로 바로 비교
        2. 딕셔너리로 mapping -> 순회 필요
        """
        # 방법 1 : 문자열 sort로 바로 비교
        # return sorted(s) == sorted(t)
    
        # 방법 2 : 딕셔너리로 mapping -> 순회 필요
        mapping = {} # 키는 알파벳, value는 사용한 횟수
        
        if len(s) != len(t) or len(set(s)) != len(set(t)):
            return False
        for a, b in zip(s, t):
            mapping[a] = mapping.get(a, 0) + 1
            mapping[b] = mapping.get(b, 0) - 1
        for v in mapping.values():
            if v < 0:
                return False
        return True
        