import sys
input = sys.stdin.readline
n, c = map(int,input().split())
n_list = [int(input()) for _ in range(n)]
answer = 0

# 가능한 조합은 1개부터 3개
# 조합 1개 
for i in range(n):
    m = int(input())
    n_list.append(m)
    if m == c:
        answer = 1

if answer == 1:
    print(answer)
else: 
    # 조합 2개 (이진 탐색)
    n_list.sort()
    left = 0
    right = n - 1
    while left <= right:
        mid = (left + right)//2
        hap = n_list(left)+ n_list(right)
        if hap == c:
            answer = 1
            break
        if hap > c:
            right = mid - 1
        else:
            left = mid + 1

`   if answer == 1:
        print(answer)
    else: 
        # 조합 3개 
    