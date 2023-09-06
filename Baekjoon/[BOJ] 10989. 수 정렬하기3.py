# 문제 : n개의 수가 주어졌을 때, 이를 오름차순으로 정렬하기 
# 내 풀이 - 병합 정렬 
n = int(input())
a = [] 
for _ in range(n) :
    a.append(int(input()))

# 병합 정렬     /