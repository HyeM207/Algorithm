class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        풀이1 . 각 단어를 정렬하여 같은지 비교하여 묶기
            - for문 돌며 각 단어 정렬
            - 딕셔너리에 키는 정렬된 단어를, 값으로는 원래 단어를 넣는다.
            - 최종적으로 딕셔너리의 값만 list 로 리턴한다. 
        """
        words = {}
        for s in strs:
            sorted_s = ''.join(sorted(s))

            words[sorted_s] = words.get(sorted_s, []) + [s]
        
        return words.values()
        