from typing import List


class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        mx = 0
        ans = 0

        for i, item in enumerate(arr):
            mx = max(mx, item)
            if mx == i:
                ans = ans + 1

        return ans
