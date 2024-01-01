#  풀이 1 (240101) : 성공
def solution(routes):
    """
    [a,b]일때 b를 오름차순 정렬 후, b를 기준으로 카메라를 세울지 말지 결정한다. 
    """
    answer = 1
    routes.sort(key=lambda x:(x[1], x[0]))
    last_cam = routes[0][1]
    
    for (a, b) in routes[1:]:
        if a > last_cam:
            last_cam = b
            answer +=1 
        
    return answer
