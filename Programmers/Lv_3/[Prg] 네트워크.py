# 문제 - lv.3
def dfs(computers, com, cnt): 
    """
    computers: 컴퓨터 배열
    com: 탐색할 컴퓨터 인덱스
    cnt: 네트워크 번호
    """
    global visited
    if visited[com] != 0:
        return 
    visited[com] = cnt 
    for idx, is_conn in enumerate(computers[com]):
        if idx != com and is_conn == 1 and visited[idx] == 0:
            dfs(computers, idx, cnt)

def solution(n, computers):
    global visited
    visited = [0]* len(computers) # 방문 안함은 0, 방문한 것은 네트워크 번호를 저장
    cnt = 0
    for i in range(n):
        if visited[i] == 0:
            cnt += 1
            dfs(computers, i, cnt)
    return cnt