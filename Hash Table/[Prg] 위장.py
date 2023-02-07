# 풀이 - lv2
'''
# #2-230208 실패 - 테스트 1에서 시간초과 걸림 
    - 정확성: 96.4
    - 합계: 96.4 / 100.0
    - 설명 : 의상 종류별 개수를 딕셔너리화한 후, 라이브러리를 이용한 조합을 써서 계산한 풀이 
'''
import collections
from itertools import combinations

def solution(clothes):
    answer = 0
    closet = collections.defaultdict()

    for c in clothes : 
        if c[1] in closet.keys():
            print(c)
            closet[c[1]] += 1
        else: 
            closet[c[1]] = 1
    
    types = list(closet.keys())
    
    # 조합 구해서 계산
    for r in range(1, len(types)+1):
        comb = list(combinations(types, r))
        
        for one_comb in comb : 
            tmp = 1
            for comb_type in one_comb:
                tmp *= closet[comb_type]
            answer += tmp
    
    return answer