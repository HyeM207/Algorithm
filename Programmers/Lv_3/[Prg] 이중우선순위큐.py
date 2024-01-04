# 풀이 1 (240104) : 성공
"""
python의 heapq를 이용함
 - 최대힙과 최소힙 만들기 : 
    heapq는 기본적으로 최솟값 추출만 지원하므로, 원소를 음수로 만들면 최댓값 추출이 가능해진다.
 - A힙에서 추출한 값*(-1)을 B힙 에서 remove로 제거한다. 
"""
import heapq

def solution(operations):
    heap_s = [] # 최솟값 추출을 위한 큐
    heap_l = [] # 최댓값 추출을 위한 큐
    
    for ops in operations:
        op, n = ops.split()
        if op == 'I': # 삽입
            heapq.heappush(heap_s, int(n)) 
            heapq.heappush(heap_l, int(n)*(-1))
        elif n == '1': # 최댓값 추출
            if heap_l:
                heap_s.remove(heapq.heappop(heap_l) *-1)
        else:  # 최솟값 pop
            if heap_s:
                heap_l.remove(heapq.heappop(heap_s) *-1)
                
    return [heapq.heappop(heap_l) *-1, heapq.heappop(heap_s)] if heap_s else [0, 0]
