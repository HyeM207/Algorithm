## 문제 - lv.3
'''
# #1-230414 성공
    정확성: 100.0
    합계: 100.0 / 100.0
    설명 : 강의 보고 dfs 문제라는 것을 참고하였고, dfs문제를 어떻게 푸는지 기억이 안나 전에 풀었던 비슷한 문제 풀이를 참고하여 풀었다. 
    참고 문제 : Graph > [LeetCode] 332. Reconstruct Itinerary.py
'''
from collections import defaultdict
def solution(tickets):
    route = []
    graph = defaultdict(list)
    
    for t in sorted(tickets, reverse=True):
        graph[t[0]].append(t[1])

    stack = ['ICN']
    while stack : 
        while graph[stack[-1]] : 
            destination = graph[stack[-1]].pop()
            stack.append(destination)
        route.append(stack.pop())
     
    return route[::-1]