# lv4 
# 이전 박테리아 문제와 거의 동일함
import sys
input = sys.stdin.readline
p, n = map(int, input().split())
virus = list(map(int, input().split()))

cnt = 0
for i in range(n):
    cnt = (cnt*p)%1000000007 + virus[i]%1000000007
print(cnt)