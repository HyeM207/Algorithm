class Solution:
    def hIndex(self, citations: List[int]) -> int:
        """
        hIndex는 n회 이상 citiation을 받은 논문이 최소 n개가 있는것.
        """
        citations.sort(reverse=True)
        
        for i, c in enumerate(citations):
            if i+1 == c:
                return c
            if i+1 > c:
                return i
    
        return len(citations)
                