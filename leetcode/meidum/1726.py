from typing import List


class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        dict_product = {}
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                ans = nums[i] * nums[j]
                if ans in dict_product:
                    dict_product[ans].append((nums[i], nums[j]))
                else:
                    dict_product[ans] = [(nums[i], nums[j])]

        num_same_product = 0
        for k in dict_product:
            if len(dict_product[k]) > 1:
                # X = X + {(n)*(n-1)}*4
                # {(n)*(n-1)} => nP2
                # 4 => permutation
                num_same_product += 4 * len(dict_product[k]) * (len(dict_product[k]) - 1)

        return num_same_product

s = Solution()
print(s.tupleSameProduct([2, 3, 4, 6]))
print(s.tupleSameProduct([1, 2, 4, 5, 10]))