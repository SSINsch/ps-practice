from typing import List


class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        new_prices = [0] * len(prices)
        for i, item in enumerate(prices):
            discount = 0
            for j, item2 in enumerate(prices[i+1:]):
                if item2 <= item:
                    discount = item2
                    break

            new_prices[i] = item - discount

        return new_prices

s = Solution()
q = [1, 2, 3, 4, 5]
ans = s.finalPrices(q)
print(ans)

q = [8, 4, 6, 2, 3]
ans = s.finalPrices(q)
print(ans)

q = [10, 1, 1, 6]
ans = s.finalPrices(q)
print(ans)
