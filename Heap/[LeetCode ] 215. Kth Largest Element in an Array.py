# Solution 1 (내 풀이)
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return sorted(nums, reverse=True)[k-1]
        
# 풀이 : 파이썬의 내장 기능 sort를 이용하여 인덱스로 접근하였다. 
# 후기 : 힙의 단원에서 sort로 풀릴 줄은 예상 못 했다. 책 풀이를 보면 heapq로 푸는 방식도 있던 데 그 방법도 알고는 있어야겠다.


# Solution 2 (책 풀이)
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for n in nums:
            heapq.heappush(heap, -n) # 음수로 저장
        
        for _ in range(1, k) :
            heapq.heappop(heap)
        
        return -heapq.heappop(heap)

# 풀이 : heapq를 이용한 풀이이다. 여기서 주목할 점은 파이썬의 heapq는 최소 힙만 지원하므로, 음수만 저장한 후 가장 낮은 수부터 추출해
#       부호를 변환하면 최대 힙처럼 동작하게 할 수 있다. 