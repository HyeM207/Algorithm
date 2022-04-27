## Greedy
- 문제를 정확히 이해하고 그에 맞는 알고리즘을 생각해내면 된다.
- 난이도가 있는 그리디의 경우 "우선순위 큐"를 이용한다. (heapq) 
- 우선 순위 큐로 안 되는 경우에는 'Counter' 모듈도 생각해보면 좋다. 

### heapq
- heapq.heappush(heap, value)
- heapq.heappop(heap)

### Counter
- counter = collections.Counter(list)
- counter.most_common(n)
- counter.subtract(value)
- counter += collections.Counter()  # 0 이하인 아이템을 목록에서 완전히 제거