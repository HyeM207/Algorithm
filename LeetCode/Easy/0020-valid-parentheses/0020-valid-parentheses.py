class Solution:
    def isValid(self, s: str) -> bool:
#         # 풀이 1: 1회 순회하며 stack과 if문 분기 이용하여 풀이함 
#         stack = []
#         match = { '}' : '{', ')' : '(', ']': '['}
        
#         for val in s:
#             if val in ('(', '[', '{'):
#                 stack.append(val)
#             elif val in (')', ']', '}'):
#                 if not stack or stack.pop() != match[val]:
#                     return False
#             else:
#                 return False
        
#         return False if stack else True 
    
        # 풀이 2: 풀이 1에서 불필요한 if문 제거함 
        stack = []
        match = { '}' : '{', ')' : '(', ']': '['}
        
        for val in s:
            if val in ('(', '[', '{'):
                stack.append(val)
                continue
            if not stack or stack.pop() != match[val]:
                    return False
        
        return False if stack else True 