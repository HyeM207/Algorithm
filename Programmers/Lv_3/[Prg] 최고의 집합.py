# 풀이 1 (240118) : 성공
from math import prod

def solution(n, s):
    """
    - 첫번째 시도 (실패) : n개로 합이 s인 모든 조합을 구함 -> 곱을 구함 
    - 깨달은 점 :  곱이 가장 큰 집합은 아래 알고리즘으로 조합을 구했을때 각 원소의 숫자들이 최대한 크게 분포한 형태이므로, 마지막 원소가 된다.
    - 두번째 시도 (성공) : 각 원소가 최대한 크도록 분포시킨다.
     
    (예시) 3,6 일 경우 조합과 곱은 아래와 같다.
    [1, 1, 4] 4
    [1, 2, 3] 6
    [2, 2, 2] 8
    """
#     def get_combi(i, last_element = 1, elements=[]): # !! 첫 번째 시도
#         #  n개로 합이 s인 모든 조합을 구하는 함수
#         result = [] 
    
#         if i == n-1:
#             for j in range(last_element, s-sum(elements)):
#                 if j > s-sum(elements)-j:
#                     break
#                 result.append([j] + [s-sum(elements)-j]) 
#             return result
#         else:
#             for j in range(last_element, s//2+1):
#                 for combi in get_combi(i+1, j, elements+[j]):
#                     result.append([j] + combi)
#         return result
    
#     if n > s :
#         return [-1]
    
#     result = get_combi(1)
    # return result[-1] if result else [-1]
  
    # !! 두 번째 시도
    if n > s :
      return [-1] 
        
    x, y = divmod(s, n)
    answer = [x] * n
    for i in range(y):
        answer[n-i-1] += 1
        
    return answer
