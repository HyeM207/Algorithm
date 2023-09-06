# 230110 시도1 - (실패: 시간초과)
import sys
input = sys.stdin.readline
n, s = map(int, input().split())

# 수열 입력 받기
nList = list(map(int, input().split()))

prefix_sum = []
tmp = 0

answer = 100001 # 거리 최대값 + 1

# 부분 합 배열 만들기
for i in nList:
    tmp += i
    if tmp >= s : 
        answer = 1
    prefix_sum.append(tmp)

# 구간 합 : i~j 까지 합 => s[j]-s[i-1]
for i in range(n-1):
    for j in range(i+1, n) :
        if i == 0 : # i-1이 음수가 되면 안되기에 if문을 둠
            hap = prefix_sum[j]
        else : 
            hap = prefix_sum[j]-prefix_sum[i-1]
        dist = j-i+1
        if hap >= s and dist < answer :
            answer = dist

# 예외 케이스 처리 (s가 0인 경우)
if s == 0:
    print(0) 
else :
    print(answer)

# 리뷰 : '부분합' 문제 제목에 맞게 정석대로 부분합 공식으로 풀었더니 시간 초과가 떴다. 
#          아무래도 투포인터를 쓰는 코드로 변경해서 시간 복잡도를 최적화해야겠다.

#####################
# # 230111 시도2 - (실패-시간초과)
import sys
input = sys.stdin.readline
n, s = map(int, input().split())

# 수열 입력 받기
nList = list(map(int, input().split()))


answer = 100001 # 거리 최대값 + 1


for left in range(n-1):
    right = left + 1
    hap = nList[left] + nList[right]
    while right <= n-1 : 
        hap += nList[right]
        # print("--", nList[left] , nList[right] , hap)
        if hap == s:
            dist = right-left+1
            # print("완성")
            if dist < answer :
                answer = dist 
                # print("갱신됨")
            break
        elif hap > s :
            # print("hap > s")
            break 
        else:
            # print("hap < s")
            right += 1

if answer == 100001:
    print(0)
else:        
    print(answer)
# 리뷰 : 투포인터 코드로 바꾸었지만, 시간초과로 실패했다. 다시 시도해봐야겠다. 