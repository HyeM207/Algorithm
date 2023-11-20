class Solution:
    # 풀이 1. 단순 구현 (코드 가독성 높임)
    """
    단순 구현
    - 0~9까지의 제곱을 모두 구해놓고 저장 
    - 이미 등장한 숫자인지 딕셔너리로 탐색  
    """  
    def isHappy(self, n: int) -> bool:
        # 제곱 미리 계산하여 저장
        square = {}
        for i in range(0, 10):
            square[str(i)] = i*i
        
        # n 검증
        existed = {} 
        hap = 0
        while hap != 1:
            hap = sum(int(square[i]) for i in str(n))
            n = hap
            if existed.get(n, 'False') is True: # 이미 등장했던 숫자인지 검토
                return False
            existed[n] = True
            
        return True if n == 1 else False
        