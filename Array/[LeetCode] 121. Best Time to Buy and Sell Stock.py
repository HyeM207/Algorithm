# Solution 1
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        
        maxPrice = -1 
        maxProfit = 0

        # 오른쪽 부터 접근하여, 가장 가격이 비싼 값(고점)과 이익이 가장 큰 값을 계산함
        for i in range(len(prices)-1, 0, -1) : 

            if prices[i] > maxPrice :
                maxPrice = prices[i]

            if (maxPrice - prices[i-1]) > maxProfit :
                maxProfit = maxPrice - prices[i-1]

        return maxProfit

# Solution 2
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        
        min_price = sys.maxsize 
        profit = 0

        for price in prices :
            min_price = min(min_price, price)
            profit = max(profit, price-min_price)
            
        return profit