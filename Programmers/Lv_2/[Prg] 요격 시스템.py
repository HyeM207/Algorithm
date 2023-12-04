# 풀이1 (231204) 성공
"""
    target만큼만 순회
    - 한 번 쏘고 이 미사일로 다음것도 처리가능한지 확인하는 로직
"""
def solution(targets): 
    targets.sort(key = lambda x: (x[1], x[0])) # **정렬을 끝나는 지점 기준으로 한다 
    shoot = targets[0][1] - 0.5
    answer = 1
    
    for t in targets[1:]:
        if t[0] <= shoot and t[1] >= shoot:
            continue
        shoot = t[1] - 0.5
        answer += 1
      
    return answer

test = [[1,2], [1,3], [1,5], [1,13],[2,3],[4,5],[4,7],[5,9],[6,12],[8,15]]
solution(test)

# 풀이1 개선 (231204) 성공
def solution(targets): 
    targets.sort(key = lambda x: x[1]) 
    shoot = -1 
    answer = 1
    
    for s, e in targets:
        if s >= shoot:
            shoot = e # 0.5 안 빼줘도 괜찮음
            answer += 1

    return answer
