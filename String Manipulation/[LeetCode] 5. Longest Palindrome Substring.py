# Solution 1
class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        palindroms = ""
        
        # 문자열의 첫글자와 끝 글자가 같은 문자열 구함 
        for startIdx, c in enumerate(s):
            sameCharIdxGroup = [i for i, ele in enumerate(s) if ele == c and i> startIdx]
 
            for endIdx in sameCharIdxGroup :
                splited_s = s[startIdx:endIdx+1]  
                
                # 문자열이 팰린드롬인지 가장 긴 팰린드롬인지 확인함
                if splited_s == splited_s[::-1] and len(splited_s) > len(palindroms) :
                    palindroms = splited_s    
                                          
        if palindroms == "":
            return s[0]
        else : 
            return palindroms


# Solution 2
class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        # 펠린드롬 판별 (이중 포인터-슬라이딩 윈도우)
        # 원리 : 중심 좌표로 부터 양쪽으로 인덱스를 늘려가며 펠린드롬인지 확인 
        def isPalindrome(left : int, right : int) -> str :
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right +=1
            return s[left+1 : right]
        
        # 예외 경우는 빠르게 리턴
        if len(s) < 2 or s == s[::-1] :
            return s
        
        # main문 
        result =''
        for i in range(len(s)-1):
            result = max(result, isPalindrome(i, i+1), isPalindrome(i, i+2), key=len)
        
        return result