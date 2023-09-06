# Solution 1 - (내 풀이_실패!)
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
    
        # times를 그래프로 전환
        graph = collections.defaultdict(list)
        for t in sorted(times): 
            graph[t[0]].append([t[1], t[2]])

            
        traced = collections.defaultdict(int) # key : 방문한 노드, value : 해당 노드까지 걸리는 시간   
        queue = [[k,0]] # 시작점인 정점을 큐에 삽입 
    
        
        while queue :
            n, t = heapq.heappop(queue) 
            
            if n not in traced :
                traced[n] = t  # 방문한 노드 저장
                
                for next_n, next_t in list(graph[n]) :
                    heapq.heappush(queue, (next_n, next_t + t)) # (다음 노드, 다음노드까지 걸리는 소요 시간을 포함한 총 시간)
        
        print(traced)
        if len(traced) != n :
            return -1
        
        return max(traced.values())



