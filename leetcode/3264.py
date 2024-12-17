from typing import List


class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        for i in range(k):
            min_v = min(nums)
            min_i = nums.index(min_v)

            new_v = min_v * multiplier
            nums[min_i] = new_v

        return nums
