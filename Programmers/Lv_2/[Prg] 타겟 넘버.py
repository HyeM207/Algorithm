## 문제 - lv.2
'''
# #1-230502 성공
    정확성: 100.0
    합계: 100.0 / 100.0
    설명 : dfs 풀이법으로 풀었다. 
'''

def solution(numbers, target):
    global answer
    answer = 0
    
    def dfs(index, result):
        global answer
        if len(numbers) == index :            
            if result == target : 
                answer += 1
            return
        dfs(index+1, result + numbers[index])
        dfs(index+1, result - numbers[index])
            
    dfs(0, 0)
    return answer