# 문제 - lv.3
answer = 0

def check(word1, word2):
    diff_cnt = 0
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            diff_cnt += 1
    return True if diff_cnt <= 1 else False

def solution(begin, target, words):
    global answer
    
    def dfs(words, word, cnt, visited):
        global answer
        if word == target:
            answer = min(cnt, answer) if answer != 0 else cnt
        for w in words:
            if check(w, word) and w not in visited:
                dfs(words, w, cnt+1, visited + [w])
            
    if target not in words:
        return 0
    dfs(words, begin, 0, [])
    return answer