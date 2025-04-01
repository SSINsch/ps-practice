from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority = nums[0]
        count = 0

        for n in nums:
            if majority == n:
                count = count + 1
            else:
                count = count - 1

            if count < 0:
                majority = n
                count = 0

        return majority


s = Solution()
print(s.majorityElement([10,9,9,9,10]))