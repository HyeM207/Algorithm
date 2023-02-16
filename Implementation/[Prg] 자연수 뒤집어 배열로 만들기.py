# 문제 -lv.1
'''
# #1-230217 성공
    정확성: 100.0
    합계: 100.0 / 100.0
    내용 : n을 str -> list한 후 [::-1]로 reverse 함
'''
def solution(n):
    answer = [int(c) for c in list(str(n))]
    return answer[::-1]

'''
(더 나은 풀이) - programmers 다른 사람 풀이 참고
def digit_reverse(n):
    return list(map(int, reversed(str(n))))

# map 기능을 이용하면 str(n)을 int형으로 바꿔 바로 list 화 가능하다.    
'''