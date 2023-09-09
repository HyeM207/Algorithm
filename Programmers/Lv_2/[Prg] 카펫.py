"""
yellow = (x-2)(y-2) 이므로 두 곱 쌍을 구해 BruteForce방식으로 x,y 구하기 (세로x >= 가로 y)
brown = xy - yellow
"""
import math
def find_prime(number):
    if number <= 1:
        return [[number, number]]
    result = []
    for i in range(1,  int(math.sqrt(number+1))+1):
        if number % i == 0 :
            result.append([i, number//i])
    return result

def solution(brown, yellow):
    answer = []
    for x, y in find_prime(yellow):
        x = x + 2
        y = y + 2
        if x*y - yellow == brown:
            answer = [y,x] 
    return answer
