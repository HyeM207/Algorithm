# 풀이 1 (240122) : 실패;시간초과
def solution(n, times):
    """
    풀이1 (실패;시간초과)  
    : heapq를 이용하여 n만큼 순회하는 풀이 (n은 1명 이상 1,000,000,000명 이하)
     - 시작시간과 종료 시간 둘 다 필요함
     - push하는 순간 한 사람은 처리되었고, 해당 desk를 사용할 수 있는 시간하고, 사용 시 종료 시간함께 저장됨
    """
    import heapq

    now_n = 0
    heap = []
    for t in times:
        heapq.heappush(heap, (t, 0)) # 종료시간이 빠른 순서대로 자동 정렬됨

    while now_n < n:
        end, start = heapq.heappop(heap)
        now_n += 1
        heapq.heappush(heap, (end+(end-start), end))
    
    return end


# 풀이 2 (240122) : 성공
def solution(n, times):
    """
    풀이2 (성공)  
    받은 힌트는 이분 탐색
        - 아이디어: 종료 시간을 담은 리스트를 만들고, n번째를 찾으라는 말인가? => No,n이 너무 큼
    결국 확인한 풀이 
        - mid를 값을 구해, 해당 mid값동안 몇 명의 사람을 처리할 수 있는지 확인후, left와 right 조정하는 풀이였다.
    """
    min_time, max_time = 1, max(times) * n

    while min_time <= max_time:
        mid_time = (min_time + max_time) // 2
        total_people = 0

        for t in times:
            total_people += mid_time // t

        if total_people >= n:
            max_time = mid_time - 1
        else:
            min_time = mid_time + 1

    return min_time
