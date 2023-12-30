# 풀이1,2 231230 : 성공
def solution(storey):
    """
    풀이1: (완전탐색) 재귀함수로 모든 경우의 수를 구함 
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

def solution(storey):
    """
    풀이 2(타풀이 참고)
     : 완전 탐색없이, "1의 자리부터 iter<=4 또는 (iter==5 and 앞자리가 없거나 앞자리<=4일때)만 내림하고 나머지 올림"하기
    """
    answer = 0
    nums = [int(digit) for digit in str(storey)[::-1]]
    
    for i in range(len(nums)):
        n = nums[i]
        if n < 5 or (n == 5 and (i+1 >= len(nums) or (i+1 < len(nums) and nums[i+1] <= 4))):  # 내림
            answer += n
        else: # 올림 
            answer += 10 - n
            if i+1 < len(nums):
                nums[i+1] += 1
            else: # <= 마지막 자리 일 경우 +1 하기
                answer += 1
                
    return answer
