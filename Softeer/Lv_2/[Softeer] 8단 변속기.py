# lv2
"""
단순 주어진 기어가 1~8까지 오름차순/내림차순인지 판단하는 문제.
오름차순인지 정석대로 확인해도 좋지만, 문자열로 비교하면 더 간단하다고 생각하여 문자열 비교로 구현함
"""
import sys
input = sys.stdin.readline
speeds = input().split()
str_speed = ''.join(speeds)
if str_speed == '12345678':
    print("ascending")
elif str_speed == '87654321':
    print("descending")
else:
    print("mixed")