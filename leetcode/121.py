from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = int(1e9)
        max_profit = 0
        for price in prices:
            if price < min_price:
                min_price = price
            profit = price - min_price
            if max_profit < profit:
                max_profit = profit
        return max_profit

s = Solution()
print(s.maxProfit([7,1,5,3,6,4]))