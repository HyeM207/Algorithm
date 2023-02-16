# 문제 - lv.1
'''
# #1-230217 성공
    정확성: 100.0
    합계: 100.0 / 100.0
    풀이 : str -> list -> sort -> join으로 문자열 변환 -> int형 변환
'''
def solution(n):
    tmp = "".join(str(i) for i in sorted(list(map(int, str(n))), reverse=True))
    return int(tmp)