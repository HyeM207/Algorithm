class Solution:
    def climbStairs(self, n: int) -> int:
        """
        1 - 1, => 1
        2 - 1+1, *2 =>2 
        3 - 1+1+1, 2+1, 1+2 => 3
        4 - 1+1+1+1, 2+1+1, 1+2+1, 1+1+2, *2+2 => 5
        5 -  =>  8
        6 -  =>  13
        7 - => 21 
        => 피보나치 수열
        f(n) = f(n-1) + f(n-2)
        이유 : f(n-1)에 1을 더한 값이 f(n)이고, f(n-2)에 2를 더한값이 f(n)이다.
        """
        mem = [1]+[2]+([0]*(n-2)) # 메모이제이션
        if n < 3:
            return n
        for i in range(2, n):
            mem[i] = mem[i-1] + mem[i-2]
        return mem[-1]