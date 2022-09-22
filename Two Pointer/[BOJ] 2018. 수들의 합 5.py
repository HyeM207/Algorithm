# 문제 : 자연수 n을 연속된 자연수 합으로 나타낼 수 있는 가지 수
# 내 풀이 1 : 시간 초과
n = int(input())
answer = 1

for i in range(1, n//2+1) :
    left = i
    right = i + 1
    hap = left + right

    while hap <= n :
        if hap == n: 
            answer += 1
            break

        right += 1
        hap += right  

print(answer) 

# 풀이 : for문으로 왼쪽 포인터는 하나씩 증가하게 하고 오른쪽은 while문 돌며 +1 해나감 
#       -> 이건 투 포인터 형식이 아닌 어찌보면 이중 for문 느낌인 풀이다. 비효율적임!

        
# 내 풀이 2 : 성공!
n = int(input()) # 1<=n<=10,000,000
answer = 1

left = 1
right = 2
hap = left + right

while left < right and right < n : 
    if hap == n :
        answer += 1
        right += 1
        hap += right
    elif hap < n :
        right += 1
        hap += right
    elif hap > n :
        left += 1
        hap -= (left-1)

print(answer)
       
# 풀이 : 투포인터는 "값에 따라 유동적으로 왼쪽과 오른쪽 포인터를 움직이는 것" 핵심으로 다시 생각해보고 값에 따라 어떤식으로 포인터를 이동해야되는지 생각해봄
#       [ 핵심 ]
#       투 포인터 시작은 왼쪽 2개 
#       1. hap이 n과 같으면 : 오른쪽 포인터 ++, 합 ++
#       2. hap이 n보다 작으면 : 오른쪽 포인터 ++, 합 ++
#       3. hap이 n보다 크면 : 왼쪽 포인터 --, 합 --

# hap이 n보다 크고/작고/같을 때 어떻게 포인터를 처리해줄지 모르겠다면 직접 그려가면서 규칙을 정해가면 풀린다! 
