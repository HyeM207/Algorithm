import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nList= list(map(int, input().split()))

s = [] # 부분 합 리스트 
prev = 0
s.append(prev)


# 부분합 구하기
for i in range(len(nList)) :
    s.append(prev + nList[i])
    prev = prev + nList[i]


# 숫자 받고 출력하기 
for _ in range(m):
    start, end = map(int, input().split())
    print(s[end]-s[start-1])

# 풀이 : 구간합 공식을 이용하여 품 
# 개선 사항 1 : 첫번째 for문에서 i를 인덱스가 아닌 nList의 원소로 쓰기