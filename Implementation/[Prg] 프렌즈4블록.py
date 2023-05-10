# 문제 - lv.2
'''
# #1-230509
    정확성: 100.0
    합계: 100.0 / 100.0 
    풀이법 : 
        1. 한 텀에 지워질 블럭들은 찾자
            - 같은게 있으면 지워야됨
        2. 지운다. 0으로 바꿈 
        3. 옮긴다?

        # 최소 4칸 ~ 최대 900칸
        # m 높이, n 폭
    개선 사항 : 
        - 리스트화 부분 : list와 map이용하여 한 줄 풀이로 바꾸기
        - 숫자 카운트 부분 : 나중에 한번에 하지 말고, 블록을 지울때 카운트 해주면 좋을것 같다.
'''
def solution(m, n, board):
    answer = 0
    # 0. 리스트화 하기 
    tmp = []
    for g in board : 
        tmp.append(list(g))
    board = tmp
    
    while True : 
        removed = []
        # 1. 지울 대상 찾기 
        for i in range(m-1): # 높이
            for j in range(n-1) : # 가로 #i,j가 왼쪽 상단 꼭짓점으로 하는 사각형 
                if board[i][j] == '0' : 
                    continue
                if board[i][j] == board [i][j+1] and board[i][j] == board[i+1][j] and board[i][j] == board[i+1][j+1] :  
                    removed.append([i,j])
        # 2. 지운다.
        if len(removed) == 0 :
            break
        for i, j in removed : 
            board[i][j] = '0'
            board[i+1][j] = '0'
            board[i][j+1] = '0'
            board[i+1][j+1] = '0'

        # 3. 옮긴다
        for j in range(n): # 열별로 확인
            for i in range(m-1, -1, -1) : # 밑에서부터 끌어당김
                if board[i][j] == '0' :
                    tmp = i-1
                    while tmp >= 0 :
                        if board[tmp][j] == '0':
                            tmp -= 1
                        else:
                            board[i][j] = board[tmp][j]
                            board[tmp][j] = '0'
                            break
    # 마지막 지워진 블럭 카운트
    for i in range(m):
        for j in range(n) :
            if board[i][j] == '0':
                answer +=1 

    return answer 