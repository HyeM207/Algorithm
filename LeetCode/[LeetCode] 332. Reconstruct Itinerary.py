# Solution 1 (내 풀이_실패!)
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:

        def dfs(departure, lastDepart = None):

            if not graph[departure] : # 출발지가 없는 경우 return False
                lastDepart = departure
                return False
            
            result.append(departure[:])
            
            for dest in graph[departure]:
                if dest[1] != 1 : # 사용한 일정이 아닌 경우일 때만 호출 
                    dest[1] = 1
                    rv = dfs(dest[0])   
                    
                    if rv == False : 
                        lastDepart = dest[0]
                        dest[1] = 0
      
        
        # 여행 일정을 정렬한 후, 그래프 형태로 바꾼다. (이유 : 중복된 일정의 경우 어휘순으로 방문하기 때문이다) 
        # 이때 사용한 여행일정인지 확인하기 위해 0과 1로 두고 디폴트를 0으로 설정해두었다. 
        graph = collections.defaultdict(list)
        for t in sorted(tickets): 
            graph[t[0]].append([t[1], 0])
        

        result = []

        dfs('JFK', '') 
       
        return result

# 풀이 : dfs를 돌며 여행일정의 목적지를 다음 dfs 순환때 출발지로 설정해두고 여행일정을 만들어가는 흐름이다. 
#       이때 이미 사용한 여행일정인지 확인하고 여행일정을 구성하게 된다.  
# 후기 : 이 문제도 계속 시도했지만 풀지 못한 문제이다. 알고리즘 자체를 잘못 생각한 것으로 보인다.. 
#       책 풀이를 통해 정확한 풀이 방법을 익혀야겠다.  
 


# Solution 2 (책 풀이 1 _DFS 풀이 최적화)
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:

        graph = collections.defaultdict(list)
        # 그래프를 뒤집어서 구성
        for a, b in sorted(tickets, reverse=True) :
            graph[a].append(b)

        route =[]
        
        def dfs(a) : 
            # 마지막 값ㅇ르 읽어 어휘 순으로 방문
            while graph[a] : 
                dfs(graph[a].pop())
            route.append(a)

        dfs('JFK')

        # 다시 뒤집어 어휘 순 결과로
        return route[::-1]

# 풀이 : 최적화 재귀 풀이. 그래프를 reverse 안 하고 pop(0)으로 하여 코드를 짤 수 있지만, pop(0)은 O(n) 이기 때문에 pop()으로 바꾸기 위해 graph를 reverse한다.
#       해당 알고리즘의 핵심은 while문으로 순회를 한 다음에 최종 경로가 담기는 route에 append 하는 것이다.
# append는 dfs를 순회하고 return 하고 나서 append 되므로 return 할때는 [::-1]로 뒤집어서 return 한다. 



# Solution 3 (책 풀이 2 _반복 풀이)
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:

        graph = collections.defaultdict(list)
        # 그래프를 뒤집어서 구성
        for a, b in sorted(tickets) :
            graph[a].append(b)

        route, stack = [], ['JFK']
        while stack : 
            # 반복으로 스택을 구성하되 막히는 부분에서 풀어내는 처리 
            while graph[stack[-1]] :
                stack.append(graph[stack[-1]].pop(0))
            route.append(stack.pop())

        # 다시 뒤집어 어휘 순 결과로
        return route[::-1]

# 풀이 : 반복 풀이, 반복으로 stack에 방문한 노드를 저장하고, route에 최종 방문 노드를 저장한다. 