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
            
       