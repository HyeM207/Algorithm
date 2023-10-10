# lv3
# 1트 실패 
import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
stones = list(map(int, input().split()))
cnt = 1
result = 0

def bfs(start_idx, queue):
    global result
    cnt = 0
    while queue:
        now_idx, cnt = queue.popleft()
        result = max(result, cnt)
        for i in range(now_idx+1, n):
            if stones[now_idx] < stones[i]:
                queue.append((i, cnt+1))

for i in range(n):
    for j in range(i+1, n):
            if stones[now_idx] < stones[i]:
                queue.append((i, cnt+1))
print(result)

# 2트 - 알고리즘 영상 보고 로직 바꿈 - 성공
import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
stones = list(map(int, input().split()))

result = [1]*n 
for i in range(n):
    max_cnt = 1
    for j in range(i):
        if stones[i] > stones[j]:
            max_cnt = max(result[j] + 1, max_cnt)
    result[i] = max_cnt
print(max(result))
