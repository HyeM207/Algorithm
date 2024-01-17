# 풀이 1 (240117) : 성공
import heapq

def solution(jobs):
    """
    사전작업. 요청 시간 순으로 작업 정렬
    1. 요청이 들어온것만 추림
    2. 소요시간 짧은 것부터 처리함 (heapq 이용)
    
    ! 목표 : jobs 길이만큼만 순회하자
    """
    total_min, i, now = 0, 0, 0
    jobs.sort(key=lambda x: x[0])    
    heap = []
    
    while i < len(jobs) or heap:
        # 들어온 요청 담음
        while i < len(jobs) and now >= jobs[i][0]:
            heapq.heappush(heap, (jobs[i][1], jobs[i][0]))
            i += 1
        
        # 처리할 요청 하나 뽑아 진행함
        if heap:
            job_time, start = heapq.heappop(heap)
            total_min += (now - start) + job_time
            now += job_time
        else:
            now = jobs[i][0]

    return int(total_min / len(jobs))
