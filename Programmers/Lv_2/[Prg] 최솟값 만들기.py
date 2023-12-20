# 문제 - lv.2
'''
# #1-230418 성공
    정확성: 69.6
    효율성: 30.4
    합계: 100.0 / 100.0
    풀이 : 작은 수를 만들려면 작은 수와 큰수를 곱한다는 원리를 이용하여 sort 하여 값을 계산한다. (lv2보단 lv.0에 가까운 문제)
'''
def solution(A,B):
    answer = 0

    A.sort()
    B.sort(reverse=True)
    for i in range(len(A)):
        answer += A[i] * B[i]

    return answer


# 풀이 2
def solution(A,B):
    """
    풀이 : 곱하고 더한 값이 최소값이 되려면, 곱할 때 가장 큰것과 가장 작은 것을 곱해야된다.
        => O(n logn) 
    """
    A.sort()
    B.sort(reverse=True)

    return sum([a * b for a, b in zip(A, B)])
