# 문제 - lv.
'''
# #1-230518 성공
    정확성: 100.0
    합계: 100.0 / 100.0
    풀이 : Counter 이용하여 개수를 카운트 -> 개수가 많은 것부터 넣기
    개선사항 : Counter에서 sorted()쓸 필요 없이, Counter의 내장 함수인 most_common()를 쓰면 된다.
'''
from collections import Counter
def solution(k, tangerine):
    answer = 0
    cnt = Counter(tangerine)
    cnt = sorted(cnt.values(), reverse=True)

    tmp = 0
    for c in cnt:
        tmp += c
        answer += 1
        if tmp >= k :
            break
    return answer