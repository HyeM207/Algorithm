# 풀이 231230 : 성공
def solution(storey):
    """
    재귀함수로 모든 경우의 수를 구해야됨 
     - 첫 아이디어 (실패): 4이하이면 빼고, 5이상이면 더하는 것을 생각했지만 예외 존재함 (2994)
     - 모든 경우의 수 dfs로 구함
    """
    def search(num, cnt):
        global answer 

        if answer < cnt: # 이미 더 작은 횟수로 성공한 사례가 있는 경우 break
            return 
        if num == 0: # 0 완성되면 break  
            answer = min(answer, cnt)
            return 
        if num < 0 : # 음수되면 break
            return 
        
        몫, 나머지 = divmod(num, 10)
        search(몫, cnt+나머지) # 나머지 버린 경우
        search(몫+1, cnt+(10-나머지)) # 나머지 올린 경우
        
    global answer
    answer = float('inf')
    search(storey, 0)
    return answer
