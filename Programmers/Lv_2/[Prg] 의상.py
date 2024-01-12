# 풀이 1 (240112) : 성공
from collections import Counter
from functools import reduce

def solution(clothes):
    closet = Counter([c_type for _, c_type in clothes])
    answer = reduce(lambda x, y: x * (y + 1), closet.values(), 1) - 1

    return answer
