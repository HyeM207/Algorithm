class Solution:
    # 풀이 1 : 정렬하여 for문 접근 => O(n log n)
    def hIndex_(self, citations: List[int]) -> int:
        """
        hIndex는 n회 이상 citiation을 받은 논문이 최소 n개가 있는것.
        """
        citations.sort(reverse=True)
        
        for i, c in enumerate(citations):
            if i+1 <= c:
                continue 
            else:
                return i
    
        return len(citations)
    
    # 풀이 2 : 정렬 없이 O(n) 도전
    """
    count 배열을 두어 인용 횟수를 저장한다.
    """
    def hIndex(self, citations: List[int]) -> int:
        c_len = len(citations)
        count = [0] * (c_len + 1)
        
        # 논문 개수 카운트
        for c in citations:
            count[min(c_len, c)] += 1
        
        # hIndex 계산
        cnt = 0
        for i in range(c_len, -1, -1):
            cnt += count[i]
            if i <= cnt:
                return i
        return cnt