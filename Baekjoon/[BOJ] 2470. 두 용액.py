import sys
input = sys.stdin.readline
n = int(input())
n_list = list(map(int, input().split()))
n_list.sort()


left = 0
right = n-1
result = 1000000000 + 10
answer = [] 
while left < right:
    mix = n_list[left] + n_list[right]
    if abs(mix) < result :
        result = abs(mix)
        answer = [n_list[left], n_list[right]]
    if mix > 0:
        right -= 1
    else:
        left += 1
print(*answer)

"""
4
-10 -8 -3 3

4
-10 1 5 -50
[-50, -10, 1, 5]

4
999999995 999999996 999999997 1000000000
"""