# Solution 1
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        
        result = 0
        
        for c in jewels:
            result += stones.count(c)
            
        return result