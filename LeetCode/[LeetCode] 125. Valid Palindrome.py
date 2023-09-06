# Solution 1
class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        check = []

        for c in s :
            if c.isalpha() or c.isdigit():
                check.append(c.lower())
    
        check_len = len(check)
       
        if check_len == 0 :
            return True
        
        for i in range(0, check_len//2 + 1):
            if check[i] != check[check_len-1-i] :
                return False
            
        return True


# Solution 2
class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        check : Deque = collections.deque()

        for c in s :
            if c.isalnum() :
                check.append(c.lower())
    
        while len(check) > 1 :
            if check.popleft() != check.pop():
                return False
    
        return True