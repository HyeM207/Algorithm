# Solution 1 - (내 풀이)
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        def cal_dist(x: int, y: int):
            return pow(abs(0-x),2) + pow(abs(0-y),2)
        
        if len(points) == 1 :
            return points
        
        dist = [] # [거리^2, 인덱스 값]
        
        # 거리 계산
        for i in range(len(points)):
            dist.append([cal_dist(points[i][0], points[i][1]), i])
            
        dist.sort()
   
        # k개 만큼 result에 담기
        result = []
        i = 0
        
        while i <= k-1 :
            result.append(points[dist[i][1]])
            i += 1
            
        return result

# 후기 : 처음에 문제를 잘못 이해하여 돌아갔던 문제다. 비교적 쉬운 문제다.
# 풀이 : 원점까지의 거리를 계산하여 dist 리스트에 [거리^2, 인덱스] 를 저장한다.
#           그런다음 k개 만큼 result에 담아 return한다. 

# Soltion 2 - (책 풀이)
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        heap = []
        for (x, y) in points:
            dist = x ** 2 + y ** 2
            heapq.heappush(heap, (dist, x, y))
        
        result = []
        for _ in range(k) :
            (dist, x, y) = heapq.heappop(heap)
            result.append((x,y))
        return result

# 후기 : 역시 책 풀이는 다르다. 더 간결하고 빠르게 풀이를 하였다.
# 풀이 : heap을 이용하여 (heap, x , y) 쌍을 heap에 저장하고 k개 만큼 heappop()하여 result에 넣어 return하는 형식이다. 
#       또한 원점까지의 거리를 x**2 + y**2로 한 것을 주목할 만하다.