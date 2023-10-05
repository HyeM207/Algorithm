# lv2
"""
첫 시도때 무작정 곱하고 큰 값을 나머지 연산하여 시간 초과남
a*b한 값을 나눈 나머지는 각각 나머지를 연산한 것과 똑같으니 이를 이용하여 해결함
"""
import sys
input = sys.stdin.readline
k, p, n = map(int, input().split())
result = k
for i in range(n):
    result = (result * p) % 1000000007
print(result)