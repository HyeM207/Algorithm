# 문제 - lv.1
'''
# #1-230225 성공
    - 정확성: 100.0
    - 합계: 100.0 / 100.0
    - 풀이 : 비트연산 OR인 것을 알아내고, format과 zfill을 이용하여 이진수를 문자열로 변환 후, replace를 이용해 벽 모양으로 바꾸는 것이 핵심이다.
'''
def solution(n, arr1, arr2):
    answer = []
    # 하나라도 1이면 1임 , (1,1) = 1 (1,0) = 1 (0,1) = 1
    # 모두 0이면 0임 (0,0) = 0 
    # 즉, 비트연산의 OR 연산이다
    for i, j in zip(arr1, arr2) :
        result = format(i | j,'b').zfill(n)
        result = result.replace("1", "#")
        result = result.replace("0", " ")
        answer.append(result)

    return answer