import sys
input = sys.stdin.readline
k, n = map(int,input().split())
n_list = [int(input()) for _ in range(k)]
left = 1
right = sum(n_list)//n

while left <= right:
    mid = (left + right) // 2
    answer = 0
    for i in n_list:
        answer += i//mid
    if answer < n:
        right = mid - 1
    else: 
        left = mid + 1
print(right)