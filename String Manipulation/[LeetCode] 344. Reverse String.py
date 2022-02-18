# Solution 1 
class Solution:
    def reverseString(self, s: List[str]) -> None:
     
        for i in range(0, len(s)//2) :
            tmp = s[i]
            s[i] = s[len(s)-1-i]
            s[len(s)-1-i] = tmp


# Solution 2
class Solution:
    def reverseString(self, s: List[str]) -> None:
        
        s.reverse()