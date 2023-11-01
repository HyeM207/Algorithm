from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # 1. 단순 딕셔너리를 이용한 풀이
#         alpha = {}
#         for m in magazine:
#             alpha[m] = alpha.get(m, 0) + 1

#         for r in ransomNote:
#             if alpha.get(r, 0) <= 0:
#                 return False
#             alpha[r] -= 1
#         return True

        # 2. Counter를 이용한 풀이
        m_count = Counter(magazine)
        r_count = Counter(ransomNote)
        m_count.subtract(r_count) 
        remain = sorted(list(m_count.values()), reverse=True)
        while remain:
            if remain.pop() < 0:
                return False
            return True