# 문제 : 각 배열의 원소 기준으로 오른쪽으로 큰 수 중 가장 왼쪽에 있는 수를 출력하는 문제 
# 책 풀이 
n = int(input())
nList = list(map(int, input().split()))
result = [0] * n # 결과를 저장하는 배열
myStack = [] # 오큰수 계산 용도. 오큰수를 찾아야하는 원소 인덱스를 저장함

for i in range(n):
    while myStack and nList[myStack[-1]] < nList[i]: # 오큰수를 찾았다면 result 배열에 저장 
        result[myStack.pop()] = nList[i]
    
    myStack.append(i)

while myStack : # 다 돌고 오큰수가 없는 인덱스는 -1로 채워준다
    result[myStack.pop()] = -1

print(*result)

# 핵심 : 스택에 무엇을 넣어야할지가 핵심임. 
#       처음에 오큰수들을 스택에 넣어야된다고 생각했는데 그게 아니라, 각 인덱스에 오큰수의 인덱스를 저장해야됐다. 헤매다가 생각못하고 결국 책 해설을 보게되었다.