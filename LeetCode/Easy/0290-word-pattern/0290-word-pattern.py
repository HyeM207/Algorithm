class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
        #  패턴의 각 문자를 key로하는 딕셔너리로 관리 => n회 순회
        mapping = {}
        words = s.split()
        
        if len(pattern) != len(words):
            return False
        for idx, p in enumerate(pattern):
            if p not in mapping.keys(): # 새로운 key일 경우 
                if words[idx] not in mapping.values():
                    mapping[p] = words[idx]
                else:
                    return False
            else:
                if mapping[p] != words[idx]: # 기존의 key 값과 다를 경우 
                    return False
        return True