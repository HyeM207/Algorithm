# Solution 1 - 내 풀이
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        
        for i in range(len(prices) - 1) : 
            if prices[i+1] > prices[i] : 
                profit += prices[i+1] - prices[i]
                
        return profit

# 풀이  : 다음날의 가격이 전날보다 높다면 바로 사고 파는 풀이로, 원리만 잘 생각하면 어렵지 않게 풀 수 있었다. 


# Solution 2 - 책 풀이
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        return sum(max( prices[i+1]- prices[i], 0) for i in range(len(prices) - 1))

# 책 풀이 : 한 줄 for문을 이용하여, max로 0이상의 profit을 더하는 간단하고 깔끔한 풀이 방법이다. 