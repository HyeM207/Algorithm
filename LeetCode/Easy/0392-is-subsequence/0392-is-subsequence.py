class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # 어렵게 생각해서 못 풀었던 문제. 간단하게 생각하자
        s_pointer = 0
        if len(s) == 0:
            return True
        for c in t:
            if s_pointer == len(s):
                return True
            if c == s[s_pointer]:
                s_pointer += 1
        return s_pointer == len(s)