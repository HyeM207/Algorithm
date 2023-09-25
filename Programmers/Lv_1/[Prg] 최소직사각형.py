# 문제 - lv.1
'''
# #1-230217 성공
    정확성: 100.0
    합계: 100.0 / 100.0
    풀이 : 가로,세로 뒤집어도 최종적으로 가로,세로 각각 가장 긴 값을 구해야된다는 점을 이용하여 품
'''
def solution(sizes):
    answer = 0
    max_width = -1
    max_height = -1
    
    # 가로, 세로 중 긴 것을 앞쪽에 배치
    # 가로와 세로 각각 max값을 곱함
    for i in range(len(sizes)):
        sizes[i] = sorted(sizes[i])
        if max_width < sizes[i][0] :
            max_width = sizes[i][0]
        if max_height < sizes[i][1] :
            max_height = sizes[i][1]
        
    return max_width*max_height

'''
더 나은 풀이 (programmers 다른 사람 풀이 참고): min과 max 함수를 for문 조합으로 풀 수 있다는 것을 알아두자
def solution(sizes):
    return max(max(x) for x in sizes) * max(min(x) for x in sizes)
'''
