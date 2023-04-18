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