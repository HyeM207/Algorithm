# 문제 - lv.2
'''
# #1-230425 성공
    정확성: 100.0
    합계: 100.0 / 100.0
    풀이 : 예전에 거의 비슷한 문제를 스택으로 풀었던 기억이 있어 스택을 활용하여 품
        - stack에는 앞에서 큰수를 찾지 못한 인덱스 번호들이 쌓이게 되고, 큰수를 찾게 되면 stack을 pop하여 result배열에 담아둔다.
        - stack에 남은 원소들은 큰수를 찾지 못한 값이므로, 원소를 다 빼서 result 배열에 -1을 넣어준다. 
'''
def solution(numbers):
    
    stack = [] 
    result = [0] * len(numbers)
        
    for i in range(len(numbers)):
        while stack and numbers[stack[-1]] < numbers[i] :
            result[stack.pop()] = numbers[i]
            
        stack.append(i)
        
    while stack : 
        result[stack.pop()] = -1
    
    return result

# 실패코드 : 처음엔 이렇게 풀었다가 스택을 이용하자는 기억이 떠올라 삭제함 
#     answer = []
#     first_bignum = [-1, 0] # 인덱스,값
    
#     for i in range(len(numbers)):
#         if i < first_bignum[0] : 
#             answer.append(first_bignum[1])
#         else : 
#             j = i + 1
#             is_find = False
#             while j < len(numbers) : 
#                 if numbers[j] > numbers[i] :
#                     first_bignum[0] = j
#                     first_bignum[1] =  numbers[j]
#                     answer.append(first_bignum[1])
#                     is_find = True
#                     break
#                 j += 1
#             if is_find == False : 
#                 answer.append(-1)
#     return answer 