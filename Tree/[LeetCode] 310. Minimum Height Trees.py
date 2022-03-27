# Solution 1 (내 풀이)
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:

        
        if n == 1 :
            return [0]
        # 그래프로 변환 
        graph = collections.defaultdict(list)
        for a, b in sorted(edges): 
            graph[a].append(b) 
            graph[b].append(a)
        
        graph = dict(graph) # for문 사용을 위해 dictionary 형식으로 바꿈
        
        n = 1   
        deletedNode = []
        
        for k in graph:
            if len(graph[k]) == n :
                deletedNode.append(k)
        
        
        # 삭제 과정        
        while len(graph) > 2:
            
            # 리프노드 삭제
            for d in deletedNode:
                neighbor = graph[d].pop() # 삭제할 리프 노드에 연결된 이웃 노드 (하나씩 들어감) 
                del graph[d] # 해당 리프 노드 삭제
                graph[neighbor].remove(d) # 이웃 노드 리스트에서 리프 노드삭제 
                
            # 삭제할 리프노드 리스트에 저장     
            deletedNode = []
            for k in graph:
                if len(graph[k]) == n :
                    deletedNode.append(k)
                    

        return graph.keys()

# 핵심 아이디어 : MHT가 되기 위해서는 트리 루트가 중간 노드가 되어야 함 
#               즉, graph로 표현 시 연결된 노드가 많을 수폭, 트리 루트가 될 확률이 높음 

# 흐름 : 연결 노드를 그래프로 표현 -> 삭제할 리프노드(: 연결된 노드가 1개) 리스트에 저장  
#    -> while문 돌며 리프노드 리스트의 리프노드와 리프노드와 연결된 이웃노드에서 삭제 -> 다음 리프노드 조사 -> 반복 -> 남은 그래프의 key값 return  


# 후기 : 연결노드를 graph로 표현하고 가장 많이 연결된 노드가 중앙이 된다는 것은 알았지만 리프노드를 삭제하는 것은 책 풀이를 보고 깨달았다.
#       깨달은 후에는 리프노드 삭제하는 코드를 혼자 짰고, 책 부분을 참고한 것은 while n < 2 와 neighbor 부분의 코드 이다.

'''
[ TEST CASE ]
10
[[0,2], [1,2],[2,3],[2,4],[3,5],[5,9],[4,6],[4,7],[7,8]]
6
[[3,0],[3,1],[3,2],[3,4],[5,4]]
4
[[1,0],[1,2],[1,3]]
1
[]
'''