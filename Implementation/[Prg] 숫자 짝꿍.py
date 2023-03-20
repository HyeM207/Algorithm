## 문제 - lv.1
'''
# #1-230320 성공
    정확성: 100.0
    합계: 100.0 / 100.0
    설명 : Counter의 교집합 연산으로, 중복된 원소 뽑아내고 이를 문자열로 바꿈 (단 0만 여러개인 경우는 예외처리해줌)
'''

import collections 

def solution(X, Y):
    answer = ''
    intersection = collections.Counter(X) & collections.Counter(Y)
    
    # 0만 있는 경우 예외처리
    if len(intersection) == 1 and intersection['0'] >= 2:
        intersection['0'] =1
    
    result = sorted(list((intersection).elements()), reverse=True)
    
    return ''.join(result) if len(result) != 0  else "-1"