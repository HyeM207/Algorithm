# Solution 1 (책 풀이)
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        # times를 그래프로 전환
        graph = collections.defaultdict(list)
        for a, b, c in flights: 
            graph[a].append((b,c))

            
        # 정점, 가격, 남은 경유지
        queue = [(0, src , k)]
    
        
        while queue  :
            price, node, k_num = heapq.heappop(queue) 
            
            if node == dst : 
                return price
            
            if k_num >= 0 :
                for v, w in list(graph[node]) :
                    heapq.heappush(queue, (price + w, v, k_num-1)) # 다음 큐에는 다음 정점 가격 더하고 경유지 -1 하여 push

        return -100

# 풀이 : BFS 문제로, 우선순위 큐 (heapq)를 이용한 문제 풀이. queue에는 앞으로 방문해야할 노드와, 가격, 남은 경유지 수가 저장이 되고, 
#           while 문을 돌며, 경유지가 남아있을 때까지 순회를 하다가 도착지에 도착하면 가격을 return 한다. 

# 핵심 :  다음 방문 노드를 큐에 push
        for v, w in list(graph[node]) :
            heapq.heappush(queue, (price + w, v, k_num-1)) # 다음 큐에는 다음 정점 가격 더하고 경유지 -1 하여 push