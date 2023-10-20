"""
예외 케이스 못 찾아 질문목록 참고함
"""

def solution(board):
    def checkBingo(charc):
        cnt = 0
        cnt_width = 0
        cnt_height = 0
        cnt_cross = 0 
        for i in range(3):
            if board[i] == charc*3: # 가로 빙고
                cnt_width += 1
            if board[0][i] + board[1][i] + board[2][i] == charc*3: # 세로 빙고
                cnt_height += 1
        # 대각선 빙고
        if board[0][0] == charc and  board[0][0] == board[1][1] and board[0][0] ==  board[2][2]:
            cnt_cross += 1
        if board[0][2] == charc and  board[0][2] == board[1][1] and board[0][2] ==  board[2][0]:
            cnt_cross += 1
        return cnt_width, cnt_height, cnt_cross
    
    #  1. 개수 체크
    cnt_o = 0
    cnt_x = 0
    cnt_width = 0
    cnt_height = 0
    cnt_cross = 0 
    for i in range(3):
        for j in range(3):
            if board[i][j] == 'O':
                cnt_o += 1
            elif board[i][j] == 'X':
                cnt_x += 1
    # 비정상 개수
    if not (cnt_o - cnt_x == 0 or cnt_o - cnt_x == 1):
        return 0
    # 2. 게임 종료 후에도 계속함
    is_cross = False
    cnt_bingo_o = 0
    cnt_bingo_x = 0
    if cnt_o >= 3:
        cnt_width, cnt_height, cnt_cross = checkBingo('O')
    cnt_bingo_o = cnt_width+ cnt_height + cnt_cross
    if cnt_x >= 3 : 
        x_cnt_width, x_cnt_height, x_cnt_cross = checkBingo('X')
        cnt_bingo_x = x_cnt_width + x_cnt_height + x_cnt_cross 
    if cnt_bingo_o > 0:
        if cnt_o != cnt_x +1:
            return 0
    if cnt_bingo_x > 0:
        if cnt_o != cnt_x:
            return 0
    if cnt_bingo_x > 0 and cnt_bingo_o > 0:
        return 0
    if cnt_bingo_o == 2: 
        if cnt_width == 2 or cnt_height == 2:
            return 0
    return 1

"""
# 추가 테스크케이스
["OOO", "OXX", "OXX"], 1
["OOO", "OOO", "XXX"], 0
["XOX", "OOO", "XOX"], 1
["OOO", "XOX", "OXX"], 1
["OOO", "XOX", "XXO"], 1
["XO.", "OXO", "XOX"], 1
["XOO", "OXO", "OOX"], 0
["OXO", "XOX", "OXO"], 1
["XOX", "OXO", "XOO"], 0
["OOX", "OOX", "XXO"], 1
["O.X", "O.X", "O.."], 1
["OOO", "XOX", "XOX"], 1
["OXX", "XOO", "OXO"], 1 
"""
