# 문제 : 정렬하는 문제
# 책 풀이 참고
# 퀵 정렬
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
A = list(map(int, input().split()))

def quickSort(S, E, K) : 
    global A
    if S < E :
        pivot = partition(S, E)

        if pivot == K : # k번째 수를 찾았으므로 종료함
            return
        elif K < pivot: # pivot의 왼쪽에 k가 있으므로 왼쪽(s ~ pivot-1)만 정렬
            quickSort(S, pivot-1, K)
        else :     # pivot의 오른쪽에 k가 있으므로 오른쪽(pivot+1 ~ e)만 정렬
            quickSort(pivot+1, E, K)


def partition(S,E):
    global A
    if S + 1 == E:
        if A[S] > A[E]:
            A[S], A[E] = A[E], A[S]
        return E


    M = (S + E) // 2
    A[S], A[M] = A[M], A[S]
    pivot = A[S]
    i = S + 1
    j = E


    while i <= j :
        while pivot < A[j] and j >0 :
            j -= 1
        while pivot > A[i] and i < len(A)-1:
            i += 1 
        if i <= j:
            A[i], A[j] = A[j], A[i]
            i += 1 
            j -= 1
    
    # i == j 피벗의 값을 양쪽으로 나눈 가운데에 오도록 함
    A[S] = A[j]
    A[j] = pivot
    return j

# main
quickSort(0, N-1, K-1)
print(A[K-1])