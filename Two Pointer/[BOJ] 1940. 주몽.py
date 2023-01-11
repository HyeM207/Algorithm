# 문제 : n개의 숫자들 중 2쌍을 뽑아 m을 만들 수 있는 가지수 구하기
# 내 풀이 1 - 성공!
n = int(input()) #  N(1 ≤ N ≤ 15,000) (중복 없음)
m = int(input()) # M(1 ≤ M ≤ 10,000,000)
nList = list(map(int, input().split()))

nList.sort()

answer = 0
left = 0    # 투 포인터는 nList의 인덱스 값을 가진다
right = n-1

while left < right :
    hap = nList[left] + nList[right]

    if hap == m:
        answer += 1
        left += 1 
    elif hap < m :
        left += 1
    elif hap > m :
        right -= 1            

print(answer)

# 풀이 : 양쪽 끝에서 부터 이동하는 투 포인터로 품. 이것저것 해보며 규칙 찾느라 시간이 걸렸다 
#       [ 핵심 ]
#       투 포인터 시작은 양쪽 끝 
#       1. hap이 m과 같으면 : 왼쪽 포인터 ++
#       2. hap이 m보다 작으면 : 왼쪽 포인터 ++
#       3. hap이 m보다 크면 : 오른쪽 포인터 ++
#       +. 오른쪽 인덱스가 벗어나면 : 왼쪽 포인터 ++

# 주의 할점은 "방향 2가지"만 가지고 규칙 짜야됨 
#           - "왼쪽 포인터 ++, 오른쪽 포인터--,오른쪽 포인터 ++" 이런식으로 방향 3개 두면 안 됨. 무한 루프 빠짐 (경험담)
#           - 문제에 따라 다를 수도 있지만 대부분 그럴일 없음

#######################
# 230111 시도2 - (성공)
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
nList = list(map(int, input().split()))

# 정렬
nList.sort()

left = 0
right = n-1
hap = nList[left]
answer = 0

while left <= n-1 and left < right: # 개선 필요 (while left<right:)

    hap = nList[left] + nList[right]

    if hap == m :
        # print(left, right, hap)
        answer += 1
        left += 1

    elif hap > m :
        right -= 1

    else : # hap < m
        left += 1


print(answer)

# 리뷰 : 첫 풀이때 left와 right 모두 앞에서 시작하는 코드로 짰는데 예외처리할 것이 너무 많아, right는 뒤에서부터 시작하는 코드로 수정했다.