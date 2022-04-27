# Solution 1 - 내 풀이 (실패)
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        # 시작점 조정
        start = 0
        while start < len(gas) :
 
            if gas[start] < cost[start] :
                start += 1
                continue
            
            fuel = 0
            
            for j in range(start,start + len(gas)) : 
                idx= j % len(gas)
                
                if fuel < 0 :
                    break
      
                fuel += gas[idx]
                fuel -= cost[idx]

            if fuel >= 0 :
                return start
            
            start += 1
            
        return -1
# 풀이 : Time Limit Exceeded로 실패. 충전량에 비해 다음 주유소까지 cost가 더 큰 경우도 제외해주었지만, time limit이 되어버렸다. 

# Solution 2 - 책 풀이 
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # 모든 주유소 방문 가능 여부 판별 
        if sum(gas) < sum(cost) : 
            return -1
        
        start, fuel = 0, 0
        for i in range(len(gas)):
            # 출발점이 안 되는 지점 판별 
            if gas[i] + fuel < cost[i] :
                start = i + 1
                fuel = 0
            else : 
                fuel += gas[i] - cost[i]
        
        return start
# 풀이 : 해당 풀이는 만족하는 정답이 반드시 한 군데만 존재한다는 점을 잘 이용하여 풀이하였다. 
#       첫째로, sum(gas) < sum(cost) 경우는 제외
#       둘째로, for문으로 전체를 방문하면서 성립되지 않는 경우는 출발점을 한 칸씩 뒤로 밀어낸다. 
#       개인적으로 for문을 이용하여, fuel += gas[i] - cost[i]로 한 줄로 표현한 것에 크게 영감받았다. "아름다운 풀이"