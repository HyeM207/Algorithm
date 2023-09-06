# Solution 1 - (내 풀이)
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        result = 0
        for i in bin(x^y)[2:]:
            if i == '1' :
                result +=1
                
        return result

# 풀이 : XOR 연산 시, 비트가 다를 경우에 1로 계산한다는 점을 이용하여 
#       XOR 연산 후, 이를 문자열로 받아 '1' 문자의 개수를 카운트하여 return 한다. 

# Solution 1 - (책 풀이)
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return (bin x^y).count('1')

# 책 풀이 : 책 풀이 역시 xor 연산을 이용하였고, count함수를 사용하여 풀이를 간단화하였다. 