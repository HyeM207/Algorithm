# lv 2
import sys
input = sys.stdin.readline
m, n, k = map(int, input().split())
secrets = list(map(int, input().split()))
inputs = list(map(int, input().split()))

s =''
for st in secrets:
    s += str(st)
input_str =''
for i in inputs:
    input_str += str(i)

if s in input_str:
    print("secret")
else:
    print("normal")