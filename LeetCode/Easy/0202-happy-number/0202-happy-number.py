class Solution:
    # 풀이 1. 딕셔너리를 이용한 단순 구현 
    """
    단순 구현
    - 0~9까지의 제곱을 모두 구해놓고 저장 
    - 이미 등장한 숫자인지 딕셔너리로 탐색  
    """  
    def isHappy_(self, n: int) -> bool:
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
    
    # 풀이 2: set을 활용한 단순 구현
    def isHappy(self, n: int) -> bool:
        seen = set()  # 이미 방문한 숫자를 기록하기 위한 집합(set)
        while n != 1 and n not in seen:
            seen.add(n)
            n = sum(int(digit) ** 2 for digit in str(n))
        return n == 1