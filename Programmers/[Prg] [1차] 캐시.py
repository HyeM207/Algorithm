# 문제 - lv.2
"""
# #1-230523 성공
    정확성: 100.0
    합계: 100.0 / 100.0
    풀이 : 캐시 교체 알고리즘 : LRU(Least Recently Used)
        - 오래된 것을 삭제
        - hit이면 1, miss이면  5
            -> hit은 큐에 있으면 ok, 이때 최근 조회를 다시 뒤로 빼주기
            -> miss는 큐에 없으면 append ,이때 길이 5맞추기
            -> cache크기 0인건 따로 처리
"""
from collections import deque
def solution(cacheSize, cities):
    answer = 0
    cache = deque()

    if cacheSize == 0:
        return 5*len(cities)
    
    for city in cities :
        city = city.upper()
        if city not in cache:
            if len(cache) == cacheSize:
                cache.popleft()
            cache.append(city)
            answer += 5
        else: 
            cache.remove(city)
            cache.append(city)
            answer += 1
    return answer