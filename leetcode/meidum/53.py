from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sub_sum, max_sum = -10000, -10000

        for idx, num in enumerate(nums):
            # if current number is bigger than sum of pervious subarry, sum again from current number
            sub_sum = max(sub_sum + num, num)
            max_sum = max(sub_sum, max_sum)

        return max_sum