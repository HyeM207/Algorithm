# 풀이 1 (240202) : 성공
def solution(A, B):
    A.sort()
    B.sort()
    idx_a = 0
    for idx_b, val_b in enumerate(B):
        if A[idx_a] >= val_b:
            continue
        idx_a += 1
        
    return idx_a
