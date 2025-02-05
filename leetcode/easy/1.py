from typing import List


class Solution:
    @staticmethod
    def binary_search(target, data):
        start, end = 0, len(data) - 1

        while start <= end:
            mid = (start + end) // 2

            if data[mid] == target:
                return mid
            elif data[mid] > target:
                end = mid - 1
            else:
                start = mid + 1

        return -1

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sorted_with_indices = sorted(enumerate(nums), key=lambda x: (x[1], x[0]))
        sorted_values = [val for _, val in sorted_with_indices]
        sorted_indices = [idx for idx, _ in sorted_with_indices]

        for i, (origin_idx, num) in enumerate(zip(sorted_indices, sorted_values)):
            idx_other = self.binary_search(target - num, sorted_values[i+1:])
            if idx_other != -1:
                return [origin_idx, sorted_indices[idx_other+i+1]]

        return [-1, -1]


s = Solution()
print(s.twoSum([2, 7, 11, 15], 9))
print(s.twoSum([3, 2, 4], 6))
print(s.twoSum([3, 3], 6))