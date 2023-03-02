# 문제 - lv.1
'''
# #1-230302 성공
    정확성: 100.0
    합계: 100.0 / 100.0
    풀이 : 최소 점수는 일치하는 개수, 최대 점수는 최소점수에 0의 개수를 더한 것이라는 규칙만 알면 쉽게 구현가능한 문제였다.
'''
def solution(lottos, win_nums):
    answer = []
    rank = { 6:1, 5:2, 4:3, 3:4, 2:5, 1:6, 0:6}
    # 최소 점수 : 일치하는 개수
    # 최대 점수 : 일치하는 개수 + 0의 개수 
    right_num = 0
    zero_num = 0
    
    for l in lottos :
        if l in win_nums:
            right_num += 1 
            
        if l == 0 :
            zero_num += 1

    answer.append(rank[right_num+zero_num])
    answer.append(rank[right_num])
    return answer