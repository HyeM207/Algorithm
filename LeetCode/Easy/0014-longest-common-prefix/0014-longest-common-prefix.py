class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        인덱스 하나씩 늘려가며 모든 단어 조회 -> 인덱스는 가장 짧은 단어 길이 만큼만
            sort&len을 쓰는게 빠를까 
        최대 약 40000번 조회 (ok)
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