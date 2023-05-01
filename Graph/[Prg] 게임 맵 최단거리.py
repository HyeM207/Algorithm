## 문제 - lv.2
'''
# #1-230502 성공
    정확성: 69.9
    효율성: 30.1
    합계: 100.0 / 100.0
    설명 : 처음엔 dfs로 풀어서 시간초과 떴는데, bfs로 풀어야되는 문제임을 깨닫고 고쳤다.
        - 해당 문제는 queue를 이용하여 방문할 수 있는 노드를 집어넣고, for문을 돌며 다음 방향으로 갈 수 있는지 확인 후 queue에 append한다.
        - 2차 시도에서 틀렸었는데, 그 이유는 width와 height를 반대로 적었어서 그랬다.
'''

def solution(maps):
    answer = -1
    dx_list = [-1,1,0,0] # 움직이는 방향 (좌, 우, 상, 하)
    dy_list = [0,0,-1,1 ]
    queue = [] # 방문할 노드
    width  = len(maps) -1
    height  = len(maps[0]) -1 #

    queue.append([0,0,1])

    while queue:
        now_x, now_y, now_cnt = queue.pop(0)
        if now_x == width and now_y == height : 
            return now_cnt
        for dx, dy in zip(dx_list, dy_list):
            next_x = now_x +  dx
            next_y = now_y + dy
            if next_x < 0 or next_y < 0 or next_x > width or next_y > height :
                continue
            if maps[next_x][next_y] == 1 :
                queue.append([next_x, next_y, now_cnt+1])
                maps[next_x][next_y] = 0
    return answer 