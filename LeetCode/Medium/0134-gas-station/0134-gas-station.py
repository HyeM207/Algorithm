class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        """
        현재 역에서 충전 -> 이동 cost 마이너스 -> 충전  -> ... 반복
        충전 & 이동을 미리 계산한 것을 이용하여 접근
        
        gas = [1,2,3,4,5]
        cost = [3,4,5,1,2]
        
        t = [-2,-2,-2,3,3] => 5
            0 1 2 3 4        
        """
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