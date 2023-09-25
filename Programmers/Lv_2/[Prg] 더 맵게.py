## 문제 - lv.2
'''
# #1-230414 성공
    정확성: 76.2
    효율성: 23.8
    합계: 100.0 / 100.0
    설명 : 강의 안 보고 문제만 봤을때는 일일히 수식 계산하려고 했는데 그렇게 하면 O(n^2)의 시간이 걸린다.
        그렇기에 heap을 사용하라는 팁을 얻어, 파이썬 라이브러리 heapq를 이용하여 간단하게 풀이하였다. 
'''
import heapq

def solution(scoville, k):
    answer = 0
    heapq.heapify(scoville)
    while len(scoville) > 0 : 
        if len(scoville) == 1 and scoville[0] < k : 
            return -1 
        if scoville[0] >= k :
            return answer 
        x1 = heapq.heappop(scoville)
        x2 = heapq.heappop(scoville)
        heapq.heappush(scoville, x1 + (x2*2))
        answer += 1
    return answer