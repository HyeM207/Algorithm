# 문제 - lv.1
'''
# #1-230218
    정확성: 100.0
    합계: 100.0 / 100.0
    설명 : list로 바꾸어 sum을 구한 후 한 줄 if문을 이용해 풀이함 
'''
def solution(x):
    return True if x % sum(list(map(int, str(x))))==0 else False


'''
# 더 나은 풀이(programmers 다른 사람 풀이 참고)  : if문과 리스트로 바꾸는 작업 없이 한 줄로 표현한 깔끔한 풀이이다.
    return n%sum(int(x) for x in str(n)) == 0
'''