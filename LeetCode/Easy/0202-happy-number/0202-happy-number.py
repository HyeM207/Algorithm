class Solution:
    def isHappy(self, n: int) -> bool:
        """
        단순 구현
        - 0~9까지의 제곱을 모두 구해놓고 저장 
        - 이미 등장한 숫자인지 딕셔너리로 탐색  
        """        
        # 제곱 미리 계산하여 저장
        square = {}
        for i in range(0, 10):
            square[str(i)] = i*i
        
        existed = {n:True} # 딕셔너리로 탐색시간 줄임
        # n 검증
        while True:
            hap = 0
            for i in str(n):
                hap += square[i]
            if hap == 1:
                return True
            n = hap
            if existed.get(n, 'False') is True: # 이미 등장했던 숫자인지 검토
                return False
            existed[n] = True
        return True if n == 1 else False
        