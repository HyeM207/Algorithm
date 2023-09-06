# Solution 1 (내 풀이)
class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n).count('1')

# 풀이 : 정수를 2진수로 바꾸어 문자열로 저장하는 파이썬의 bin()함수를 이용하여 쉽게 풀이하였다.


# Solution 2 (책 풀이)
class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n : 
            n &= n -1
            count += 1
        return count 

# 책 풀이 : n값과 n-1을 AND 연산 시 비트 1이 사라진다는 점을 이용한 풀이이다. (비트 연산 이용한 풀이)

