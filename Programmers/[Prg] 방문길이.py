# 문제 - lv.2
'''
# #1-230509
    정확성: 100.0
    합계: 100.0 / 100.0 
    풀이 : 방문한 거리를 walked 리스트에 정렬해서 append하는 식으로 저장했다.
    개선사항 : 내 풀이는 그래프가 5*5로 한정되어 있어서 풀 수 있었던 문제로, 시간이 많이 걸리는 풀이다.
            -> 121개의 visited 노드로 바꿔서 풀면 더 좋을 듯하다  
'''
def solution(dirs):
    move = { 'U' : [0,1] , 'D': [0,-1] , 'R': [1,0], 'L' : [-1,0]} 
    now = [0,0]
    walked = []
    for d in dirs :
        tx = now[0] + move[d][0]
        ty = now[1] + move[d][1]
        if tx >= -5 and tx <= 5 and ty >=-5 and ty <=5 :
            moving = sorted((now, [tx,ty]))
            if moving not in walked : 
                walked.append(moving)   
            now = [tx, ty]       
    return len(walked)