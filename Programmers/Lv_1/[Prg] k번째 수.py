# 문제 - lv.1 
'''
# #1-230222 성공
    정확성: 100.0
    합계: 100.0 / 100.0
    풀이 : 문제에서 주어진 조건을 순서대로 코딩하면 쉽게 풀이 가능하다.
'''
def solution(array, commands):
    answer = []
    # i번째에서 j번째까지 부분 리스트 추출 후, 정렬해서 k번째 수 구하기
    for i,j,k in commands:
        answer.append(sorted(array[i-1:j])[k-1])
        
    return answer
