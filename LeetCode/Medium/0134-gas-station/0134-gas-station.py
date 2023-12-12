class Solution:
    # 풀이 1: 출발 가능한 시작점을 위치잡아 순회 O(N^2) 
    def canCompleteCircuit_(self, gas: List[int], cost: List[int]) -> int:
        answer = -1
        amount = 0
        start = 0
        n = len(gas)
        
        while start < n:
            # 출발 가능한 것(=양수)인것만 시작
            if gas[start] >= cost[start] :
                amount = 0
                for i in range(n):
                    amount += gas[(start + i) % n] - cost[(start + i) % n]
                    if amount < 0:
                        break
                if amount >= 0:
                    return start
                else:
                    start = (start + i) # 실패한 곳부터 start 인덱스 재설정
            start += 1
        return -1
    
    
    # 풀이 2: 한 번 순회 도전 O(n)
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # 불가능한 경우 미리 제외
        if sum(gas) - sum(cost) < 0 :
                return -1
            
        answer = 0
        tank = 0
        
        for i in range(len(gas)):
            tank += gas[i] - cost[i] # 포인트!! ==> 가스와 비용의 차이를 누적
            if tank < 0: # 음수면, 현재까지의 출발지점들은 불가하다는 의미
                tank = 0
                answer = i+1
        return answer