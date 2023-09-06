# 문제 : 주어진 문자열을 내림차순으로 정렬하는 문제 
# 내 풀이(선택 정렬) - 성공 
a = list(input())

for i in range(len(a)):
    # 최댓값의 인덱스 구하기
    maxIdx = i 
    for j in range(i+1, len(a)):
        if int(a[maxIdx]) < int(a[j]) :
            maxIdx = j

    # 최댓값 swap
    if maxIdx != i : 
        a[i], a[maxIdx] = a[maxIdx], a[i]

print(''.join(a)) 
