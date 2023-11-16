class Solution:
    # 풀이1. 한 바퀴 순회하며 최소 가격과 해당 가격 대에서 최소 가격의 최대차를 구하여 max_profit을 구한다. => O(N)
    """
    목표 : 최대 한 번만 순회해서 풀자
    7 5 1 10 11 13  -> 1 13
    13 16 11 14 15 -> 11 15
    7 10 1 2 -> 7 10
    """
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        min_price = prices[0]
        
        for price in prices[1:]:
            if min_price > price:
                min_price = price
                continue
            if price-min_price> profit:
                profit = price-min_price
    
        return profit
        