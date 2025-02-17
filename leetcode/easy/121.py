from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp_max_list = []
        max_num = 0
        for p in prices[::-1]:
            if p > max_num:
                max_num = p
            dp_max_list.append(max_num)
        dp_max_list = dp_max_list[::-1]

        max_profit = 0
        for p, max_num in zip(prices, dp_max_list):
            profit = max_num - p
            if profit > max_profit:
                max_profit = profit

        return max_profit


s = Solution()
print(s.maxProfit([7,1,5,3,6,4]))
print(s.maxProfit([7,6,4,3,1]))
