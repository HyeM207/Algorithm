# 문제 : 1~n까지 오름차순 숫자들을 스택에 넣고 pop하여 나온 숫자들의 배열이 입력 수열과 같도록 하는 스택 연산 순서 계산
# 내 풀이 - 성공
n = int(input()) # 1 ≤ n ≤ 100,000
a = []
stack = []
result = ""
flag = True 

for _ in range(n):
    a.append(int(input()))

tmp = 0 # 추가 되는 수 기억하기 위한 변수

for element in a:
    
    if tmp <= element  :
        for i in range(tmp+1, element+1):
            stack.append(i) 
            result += "+\n"
        tmp = element

    while stack :
        result += "-\n"
        if stack.pop() == element :
            break
        else :
            flag = False
            break

if flag == True:
    print(result)
else :
    print("NO")

# 풀이 : 스택을 이용하여 품. 스택에 append한 마지막 숫자를 tmp에 저장하여, 주어진 배열의 원소보다 작으면 (=스택에 넣지 않은 수이면) append 하도록 한다. 
#       pop할 때는 주어진 수열과 비교하고 맞지 않다면 flag값을 false로 설정하고 "NO" 출력한다. 

# 후기 : 내 풀이는 시간이 많이 소요되어 책처럼 효율적으로 바꿔야겠다. 

# 책 풀이 
n = int(input()) # 1 ≤ n ≤ 100,000
a = [0]*n

for i in range(n):
    a[i] = int(input())

stack = []
flag = True 
result = ""
num = 1

for i in range(n):
    su = a[i]
    if su >= num : # append 해줌 
        whlie su >=num :
            stack.append(num)
            num += 1
            answer += "+\n"
        stack.pop()
        answer += "-\n"
    else : # pop 연산
        n = stack.pop()
        if n > su :
            print("NO")
            result = False 
            break
        else : 
            answer += "-\n"

if result :
    print(answer)