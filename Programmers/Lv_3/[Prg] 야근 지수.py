# 풀이 1 (240130 ) : 성공
"""
풀이1. 가장 큰수를 없애나가자
  => heapq를 이용함
"""
import heapq 
def solution(n, works):
    # 최대힙 만들기
    max_heap = [-work for work in works]
    heapq.heapify(max_heap)
    
    # 가장 큰수부터 1씩 빼가기
    for i in range(n):
        max_val = heapq.heappop(max_heap)
        if max_val > -1:
            return 0
        max_val += 1
        heapq.heappush(max_heap, (max_val))   
    
    # 야근 지수 계산
    answer = sum([work**2 for work in max_heap])
        
    return answer
