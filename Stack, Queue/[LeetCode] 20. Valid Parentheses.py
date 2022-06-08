# Solution 1
class Solution:
    def isValid(self, s: str) -> bool:
    
        checkStack = []
        brackets = { '(' : ')', '{' : '}' , '[' : ']' } # bracket 쌍 보관
        
        for c in s :
            if c in list(brackets.keys()):
                checkStack.append(c)
            else :    
                if checkStack : 
                    if brackets[checkStack.pop()] != c :  
                        return False
                else : 
                    return False
                
       
        # bracket이 안 닫힌 경우
        if checkStack :
            return False
        else :
            return True
            

# Solution 2 (2회독_220608_성공)
class Solution:
    def isValid(self, s: str) -> bool:
        
        pairs = { '(' : ')', '{' : '}', '[' : ']' }
        stacks = []
        
        for c in s :
            if c in pairs.keys() :
                stacks.append(c)
            
            elif len(stacks) == 0 or c != pairs[stacks.pop()] : 
                return False 
        
        if stacks : 
            return False
        
        return True

# 후기 : 풀고나서 보니, 1차 풀이와 동일하게 풀었다.