# lv3
# 1트- 실패 (시간초과)
"""
공략 실패. 모든 경우의 수를 구하려고 했지만 그럴 필요없이
정렬할때 끝나는 시간이 짧은것도 고려하여 정렬하면 된다.
"""
import sys
input = sys.stdin.readline
n = int(input())
classes = []

for _ in range(n): # 입력받아 저장
    a, b = map(int, input().split())
    classes.append([a, b])
classes.sort() # 정렬

# 시작 시간을 달리하며 모든 경우의 수 확인
max_cnt = 0 
for start_idx in range(len(classes)):
    idx = start_idx
    cnt = 1
    end = classes[start_idx][1]
    while idx < len(classes):
        if idx + 1 < len(classes) and end <= classes[idx+1][0]:
            cnt += 1
            end = classes[idx+1][1]
        idx += 1
    if max_cnt < cnt:
        max_cnt = cnt 
print(max_cnt)

# 2트 - 참고하여 성공
"""
[ 핵심 부분 ]
1. heapq 사용
2. 정렬시 end time이 빠른 순으로 하기
"""
import sys
input = sys.stdin.readline
import heapq
n = int(input())
classes = []

for _ in range(n): # 입력받아 저장
    a, b = map(int, input().split())
    heapq.heappush(classes, (b, a)) # 끝나는 시간이 빠른 순으로 자동 정렬

cnt = 0
last_end = 0
while classes:
    end, start = heapq.heappop(classes)
    if last_end <= start:
        cnt += 1
        last_end = end 
print(cnt)