'''
# #1-230518 성공
    정확성: 100.0
    합계: 100.0 / 100.0
    풀이 : 단순 구현. Counter 이용하여 개수 새고, 반복문 돌며 반복 횟수 카운트함
'''
from collections import Counter
def solution(s):
    cnt_iter = 0
    cnt_removed = 0
    while s !="1":
        cnt = Counter(s)
        cnt_removed += cnt['0']
        s = str(bin(cnt['1']))[2:]
        cnt_iter += 1
    return [cnt_iter, cnt_removed]