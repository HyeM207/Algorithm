# 문제 : N개의 수 중에서 어떤 수가 다른 수 두 개의 합이 되는 경우의 수 
# 내 풀이 1 - 실패 (아래 예외를 생각 못 함)
n = int(input())
nList = list(map(int, input().split()))

nList.sort()
answer = 0

def find(left, right, target):
    global answer
    while left < right : 
        hap = nList[left] + nList[right]
        if hap == target:
            answer += 1
            print(f"left : {nList[left]} right : {nList[right]} hap : {hap}")
            break 
        elif hap > target :
            right -= 1
        else : 
            left += 1   
            
if n >= 3:
    for t in range(2, n): 
        find(0, t-1, nList[t])

print(answer)

# 예외를 조심해야됨 : (nList중에 중복이 들어갈 수 있음. 단 자기 자신을 더하는 건 안 됨) 
'''
3
0 3 3
-> 2

3
0 0 3
-> 1

3
0 0 0
-> 3
'''

# 내 풀이(+책 풀이 조금 참고) 2 - 성공
n = int(input())
nList = list(map(int, input().split()))

nList.sort()
answer = 0

def find(left, right, target):
    global answer
    while left < right : 
        hap = nList[left] + nList[right]
        if hap == nList[target]:
            if left != target and right != target: # 수정 사항
                answer += 1
                break 
            elif left == target : # 수정 사항
                left += 1
            elif right == target: # 수정 사항
                right -= 1 
        elif hap > nList[target] :
            right -= 1
        else : 
            left += 1   
   
            
if n >= 3:
    for t in range(n): 
        find(0, n-1, t) # 수정 사항 (삽질 했던 부분) right가 t-1이 아닌 n-1로 바꿔야 된다....

print(answer)