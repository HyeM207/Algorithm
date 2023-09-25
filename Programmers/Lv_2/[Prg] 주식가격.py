# 문제 - lv.2
'''
# #1-230503 성공
    정확성: 100.0
    합계: 100.0 / 100.0
    풀이 : 오큰수 문제를 반대로 구현하면 되는 비슷한 유형. 스택을 이용하여 풀었다. 
        - for문을 돌며 기본적으로 stack에 해당 인덱스를 저장하는데, 
        만약 스택에 값이 있고, 값이 작아진다면(=값이 떨어짐) stack에서 pop하여 result배열에 떨어지지 않은 기간을 기록함
'''
def solution(prices):
    answer = [0] * len(prices)
    stack = []
    
    for i in range(len(prices)) :
        while stack and prices[stack[-1]] > prices[i] :
            idx = stack.pop()
            answer[idx] = i-idx
        stack.append(i)
    
    while stack :
        idx = stack.pop()
        answer[idx] = len(prices) - idx - 1
    
    return answer