from collections import Counter
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # 1. 개수대로 맵핑 
        if len(set(s))!= len(set(t)) : # 1차 필터링
            return False
        
        mapping = {}
        for idx, c in enumerate(s):
            if c not in mapping.keys():
                mapping[c] = t[idx]
            else:
                if mapping[c]!= t[idx]:
                    return False 
        return True
        