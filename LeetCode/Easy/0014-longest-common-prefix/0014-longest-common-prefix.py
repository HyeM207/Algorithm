class Solution:
    # 풀이 1: 이중for문 -> O(NM) ;M은 가장 짧은 문자열의 길이
    def longestCommonPrefix_(self, strs: List[str]) -> str:
        """
        인덱스 하나씩 늘려가며 모든 단어 조회 -> 인덱스는 가장 짧은 단어 길이 만큼만
        최대 약 40000번 조회
        """
        answer = ""
        sorted_strs= sorted(strs, key= lambda x: len(x))
        
        for i in range(len(sorted_strs[0])):
            letter = sorted_strs[0][i]
            for c in sorted_strs[1:]:
                if letter != c[i]:
                    return answer
            answer += letter
        return answer
    
    # 풀이 2 : for문 1회
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        min_len = min(len(s) for s in strs)
        answer = ""

        for i in range(min_len):
            if all(s[i] == strs[0][i] for s in strs): # all 사용하여 코드 간단히 함
                answer += strs[0][i]
            else:
                break
                
        return answer
        
        