from typing import List


class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        result = 0

        # we consider only if the length of each list is odd.
        # if even, XOR results => all zero (a XOR a = 0)
        if len(nums2) % 2:
            for num in nums1:
                result = result ^ num

        if len(nums1) % 2:
            for num in nums2:
                result = result ^ num

        return result
