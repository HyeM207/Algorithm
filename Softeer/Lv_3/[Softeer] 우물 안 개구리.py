# lv3 
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
weight = list(map(int, input().split()))
result = [True] * n
for i in range(m):
    a, b = map(int, input().split())
    a_w = weight[a-1]
    b_w = weight[b-1]
    if a_w == b_w :
        result[a-1] = False
        result[b-1] = False
    elif a_w < b_w:
        result[a-1] = False
    else : 
        result[b-1] = False
cnt = 0 
for r in result:
    if r:
        cnt += 1
print(cnt)
"""
최고 = 누구와도 친분 x, 친분중에서 제일 무거움

1. 처음엔 다 최고
2. 친분 계산 후 같거나 작으면 (=지면) lose 
3. 최고만 남으면 그걸 count
"""