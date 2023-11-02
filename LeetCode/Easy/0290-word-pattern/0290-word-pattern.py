class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
        #  풀이 1. 패턴의 각 문자를 key로하는 딕셔너리로 관리 => n회 순회
#         mapping = {}
#         words = s.split()
        
#         if len(pattern) != len(words):
#             return False
#         for idx, p in enumerate(pattern):
#             if p not in mapping.keys(): # 새로운 key일 경우 # if p not in mapping:
#                 if words[idx] not in mapping.values():
#                     mapping[p] = words[idx]
#                 else:
#                     return False
#             else:
#                 if mapping[p] != words[idx]: # 기존의 key 값과 다를 경우 
#                     return False
#         return True

        # 풀이 2. if 필터링 후 n회 순회, if-elif-else문으로 코드 간단화함
        mapping = {}
        words = s.split()
        if len(set(pattern)) != len(set(words)):
            return False
        if len(words) != len(pattern):
            return False
        
        for i in range(len(pattern)):
            if pattern[i] not in mapping:
                mapping[pattern[i]] = words[i]
            elif mapping[pattern[i]] == words[i]:
                continue # 중복 적재 막음
            else:
                return False
        return True

        # 풀이 3. 딕셔너리 2개 활용 -> .values() 할 필요 없어짐
        words = s.split()
        if len(words) != len(pattern):
            return False

        mappingPW = {}
        mappingWP = {}
        for p,w in zip(pattern,words):
            if p not in mappingPW:
                if w in mappingWP:
                    return False
                else:
                    mappingPW[p] = w
                    mappingWP[w] = p
            else:
                if mappingWP[p] != w:
                    return False           
        return True