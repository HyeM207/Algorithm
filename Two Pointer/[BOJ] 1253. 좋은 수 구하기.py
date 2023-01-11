# 문제 : N개의 수 중에서 어떤 수가 다른 수 두 개의 합이 되는 경우의 수 
# 내 풀이 1 - 실패 (아래 예외를 생각 못 함)
# n = int(input())
# nList = list(map(int, input().split()))

# nList.sort()
# answer = 0

# def find(left, right, target):
#     global answer
#     while left < right : 
#         hap = nList[left] + nList[right]
#         if hap == target:
#             answer += 1
#             print(f"left : {nList[left]} right : {nList[right]} hap : {hap}")
#             break 
#         elif hap > target :
#             right -= 1
#         else : 
#             left += 1   
            
# if n >= 3:
#     for t in range(2, n): 
#         find(0, t-1, nList[t])

# print(answer)

# 예외를 조심해야됨 : (nList중에 중복이 들어갈 수 있음. 단 자기 자신을 더하는 건 안 됨) 
'''
3
0 3 3
-> 2

3
0 0 0
-> 3
'''

# 내 풀이(+책 풀이 조금 참고) 2 - 성공
# n = int(input())
# nList = list(map(int, input().split()))

# nList.sort()
# answer = 0

# def find(left, right, target):
#     global answer
#     while left < right : 
#         hap = nList[left] + nList[right]
#         if hap == nList[target]:
#             if left != target and right != target: # 수정 사항
#                 answer += 1
#                 break 
#             elif left == target : # 수정 사항
#                 left += 1
#             elif right == target: # 수정 사항
#                 right -= 1 
#         elif hap > nList[target] :
#             right -= 1
#         else : 
#             left += 1   
   
            
# if n >= 3:
#     for t in range(n): 
#         find(0, n-1, t) # 수정 사항 (삽질 했던 부분) right가 t-1이 아닌 n-1로 바꿔야 된다....

# print(answer)

#################
# 230111 시도 3 - (실패 -> 성공)
import sys
input = sys.stdin.readline
n = int(input())
nList = list(map(int, input().split()))

nList.sort()

answer = 0

# for t in range(2,n): 
for t in range(n): # 수정한 부분
    # 투 포인터 (양끝에서 시작)
    left = 0
    # right = t - 1
    right = n-1 # 수정한 부분
    target = nList[t]

    while left < right :  
        hap = nList[left] + nList[right]

        if hap == target :
            if left != t and right != t: 
                answer += 1
                break  
            elif left == t : #생각 못한 부분
                left +=1 
            elif right == t: #생각 못한 부분
                right -= 1
        elif hap > target :
            right -= 1 
        else: # hap < target
            left += 1

print(answer)
# 리뷰 : 투포인터 양끝 전략부터 시작하길 잘 했다. 다만 0이 포함되는 테스트케이스를 생각못했다. 이를 해결하니 성공했다. 