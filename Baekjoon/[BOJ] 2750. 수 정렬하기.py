# 내 풀이 1 (sort) - 성공
n = int(input())
a = []
for i in range(n) : 
    a.append(int(input()))

a.sort()

for e in a:
    print(e)


# 내 풀이 2 (버블 정렬) - 성공
n = int(input())
a = []
for i in range(n) : 
    a.append(int(input()))

for i in range(0, n-1):
    for j in range(0, n-1-i):
        if a[j] > a[j+1] : 
            a[j+1], a[j] = a[j], a[j+1]


for e in a:
    print(e)
