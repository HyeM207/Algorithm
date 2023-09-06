# 문제 : 주어진 문자열에서 정해진 크기의 슬라이딩 윈도우 안에 조건대로 원소가 있는지 확인하는 문제

# 내 풀이 (여러번 시도하다가 안 되어 외부 블로그 코드 부분 참고함) : 통과
# 참고한 블로그 : https://sangminlog.tistory.com/entry/boj-12891
dnaLen, partLen = map(int, input().split())
dnaStrings = input()
tmp = list(map(int, input().split()))

prequisite = {'A' : tmp[0], 'C' : tmp[1], 'G' : tmp[2], 'T' : tmp[3]}
leftDna = {'A' : 0, 'C' : 0, 'G' : 0, 'T' : 0}
answer = 0


# 슬라이딩 윈도우 양 끝의 인덱스 값을 가지는 포인터 
left = 0
right = partLen - 1

while right < dnaLen :
    if left == 0 : 
        for c in range(right+1):
            leftDna[dnaStrings[c]] += 1 
    else : 
        leftDna[dnaStrings[right]] += 1 
        leftDna[dnaStrings[left-1]] -= 1 

    check = True

    for c in ('A', 'C', 'G', 'T'):
        if prequisite[c] > leftDna[c] :
            check = False

    if check == True :
        answer+=1 

    right += 1 
    left += 1
    

print(answer)

