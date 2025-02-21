from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        cur_left = 0
        cur_right = len(nums) - 1

        while cur_left <= cur_right:
            cur = (cur_left + cur_right) // 2

            if nums[cur] == target:
                return cur
            elif target > nums[cur]:
                cur_left = cur + 1
            else :
                cur_right = cur - 1

        return -1