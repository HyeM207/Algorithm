from collections import Counter
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # 1차 풀이 (필터링 있이) => 40ms
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
    
        # 2차 풀이 (필터링 없이) => 47ms 
        # mapping = {}
        # for idx, c in enumerate(s):
        #     if c not in mapping.keys():
        #         if t[idx] not in mapping.values():
        #             mapping[c] = t[idx]
        #         else:
        #             return False
        #     else:
        #         if mapping[c]!= t[idx]:
        #             return False 
        # return True
        