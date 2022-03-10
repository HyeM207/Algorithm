# Solution 1
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        result = 0
        
        for front in range(len(s)) :
            str_dict = {}
            str_dict[s[front]] = 1
            rear = front + 1
            
            while rear < len(s) : # len 길이는 공백 포함한 길이
                if s[rear] in str_dict :
                    break
                str_dict[s[rear]] = 1
                rear += 1
                
            result = max(result, rear-front)   
        
        return result 