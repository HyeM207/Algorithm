# 문제 - lv 0
'''
# #1-230208 
    - 정확성: 100.0
    - 합계: 100.0 / 100.0
    - 풀이 : for문으로 끝 인덱스부터 접근해서 문자열 합쳤다.
'''
def solution(my_string):
    answer = ''
    for i in range(len(my_string)-1,-1, -1):
        answer += my_string[i]
    return answer

'''
풀이 추천 
    return my_string[::-1] 하면 간단히 해결된다.
'''