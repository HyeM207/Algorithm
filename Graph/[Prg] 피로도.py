# 문제 - lv.2
'''
# #1-230428 성공
    정확성: 100.0
    합계: 100.0 / 100.0
    풀이 : 던전을 탐험하는 순서의 모든 경우의 수를 구해서 체력 조건이 될때까지 방문 -> 최대 방문 값 return
        - 파이썬 라이브러리 permutations 덕분에 풀 수 있었다
    개선사항 : 몇몇 기업에서는 itertools 사용을 제한한다고 한다. 그렇기에 dfs 완전 탐색으로 직접 구현해보는걸로 하자
'''
import itertools 
def solution(k, dungeons):
    answer = []
    
    for dungeons in itertools.permutations(dungeons, len(dungeons)) :
        health = k
        cnt = 0 
        for d in dungeons : 
            if health < 0 or health - d[0] < 0:
                break
            health -= d[1]
            cnt += 1
        if health >= 0 :
            answer.append(cnt)
    return max(answer)

'''
# #2-230428 성공
    정확성: 100.0
    합계: 100.0 / 100.0
    풀이 : #1로직 그대로 이용하여 dfs함수를 구현하였다
'''
def permute(nums) :
    results = []
    prev_elements = [] 

    def dfs(elements) :
        if len(elements) == 0 : 
            results.append(prev_elements[:])
        
        for e in elements:
            next_elements = elements[:] #
            next_elements.remove(e) 
            
            prev_elements.append(e)
            dfs(next_elements[:])
            prev_elements.pop()

    dfs(nums)
    return results    
    
def solution(k, dungeons): # main 문제
    answer = []
    
    for dungeons in permute(dungeons) :
        health = k
        cnt = 0 
        for d in dungeons : 
            if health < 0 or health - d[0] < 0:
                break
            health -= d[1]
            cnt += 1
        if health >= 0 :
            answer.append(cnt)
    return max(answer)
