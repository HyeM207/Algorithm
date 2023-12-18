class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        풀이 1 : 다른 풀이 참고함. DP Bottom-up 
        dp[i]는 문자열 s[:i+1]가 주어진 단어 사전(wordDict)을 이용하여 나눌 수 있는지 여부
        """
        if not wordDict: 
            return False
        
        wordDict = set(wordDict) # 중복 제거 및 해시테이블화
        m = len(max(wordDict, key=len)) # wordDict 중 가장 긴 단어
        dp = [False] * (len(s) + 1) 
        dp[0] = True
        
        for i in range(len(s)):
            if dp[i]: # 메모이제이션
                for j in range(i, min(len(s), i+m)):
                     if s[i: j+1] in wordDict:
                        dp[j+1] = True
                if dp[-1]:
                    return True
        return dp[-1]