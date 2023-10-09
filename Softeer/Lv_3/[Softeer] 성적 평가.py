# lv3
import sys
input = sys.stdin.readline 
n = int(input())
total = [] # 입력값 그대로
results = [] # 출력할 랭킹 결과 
# 입력
for _ in range(3):
    tmp = list(map(int, input().split()))
    total.append(tmp)

# 전체 합산
total_hap = [] 
for j in range(n):
    hap = 0
    for i in range(3):
        hap += total[i][j]
    total_hap.append(hap)
total.append(total_hap)

# 정렬 후 랭킹 계산
for tmp in total:
    contest = {}
    for idx, value in enumerate(tmp):
        contest[idx] = value
    s = sorted(contest.items(), key=lambda x:x[1], reverse=True)
    
    result = [None] * n
    prev_score = -1
    prev_rank = -1 
    for rank, (idx, value) in enumerate(s): # 랭킹 계산 
        if prev_score != -1 and prev_score == value:
            result[idx] = prev_rank
            prev_rank = prev_rank
        else: 
            result[idx] = rank+1
            prev_rank = rank+1
        prev_score = value
    results.append(result)

# 결과 출력
for result in results:
    print(' '.join(str(x) for x in result))