"""
20-7 = 13
"""
import sys
input = sys.stdin.readline
n, m = map(int,input().split())
n_list = list(map(int, input().split()))
n_list.sort(reverse=True)

def gap():

for i in n_list:
    gap(i)


