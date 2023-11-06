class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        match = { '}' : '{', ')' : '(', ']': '['}
        
        for val in s:
            if val in ('(', '[', '{'):
                stack.append(val)
            elif val in (')', ']', '}'):
                if not stack or stack.pop() != match[val]:
                    return False
            else:
                return False
        
        return False if stack else True 