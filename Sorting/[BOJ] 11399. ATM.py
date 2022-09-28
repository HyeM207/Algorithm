# 문제 : 줄을 서는 순서에 따라 돈을 인출하는데 필요한 시간 합이 달라지는데, 최소 시간 합을 구하는 문제
# 풀이 : 인출하는 시간이 적은 순서대로 정렬한다 
n = int(input())
a  = list(map(int, input().split()))

# 정렬하기 - 삽입정렬
# a.sort()

for i in range(1, len(a)):
    flag = False
    tmp = 0
    for j in range(0, i+1):
        if flag == False and a[j] > a[i]:
            flag = True
            tmp = a[i]
        if flag == True : 
            a[j], tmp = tmp, a[j]
            
# print("a" , a)
# 합 구하기 
prevSum = 0
total = 0
for e in a:
    prevSum += e
    total += prevSum

print(total)
