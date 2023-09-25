# lv.2
answer = -1
def solution(match):
    dic= {}
    alphas  = ['A', 'E', 'I', 'O', 'U']
    
    def dfs(word):
        global answer
        if len(word) > 5: 
            return
        answer += 1
        dic[word] = answer
        if len(word) == 5:
            return
        for alpha in alphas:
            dfs(word+alpha)
    dfs("")
    return dic[match]