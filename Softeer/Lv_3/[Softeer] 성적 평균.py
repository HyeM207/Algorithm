#  lv3
import sys
input = sys.stdin.readline
n, k = map(int, input().split())
scores = list(map(int, input().split()))
for _ in range(k):
    x, y = map(int, input().split())
    result = round(sum(scores[x-1:y]) / (y-x+1), 2)
    print("%0.2f"%result)