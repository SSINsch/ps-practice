from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        new_start, new_end = newInterval[0], newInterval[1]
        ans = []

        for idx, item_interval in enumerate(intervals):
            start_i, end_i = item_interval[0], item_interval[1]

            # if newInterval has bigger start number than existing interval,
            # it cannot overlap, so just add the existing one
            if end_i < new_start:
                ans.append(item_interval)

            # if newInterval has smaller end number than existing interval,
            # add the new one, and remaining items
            elif new_end < start_i:
                ans.append([new_start, new_end])
                ans = ans + intervals[idx:]
                return ans

            # if overlapped, renew the interval
            else:
                new_start = min(new_start, start_i)
                new_end = max(new_end, end_i)

        ans.append([new_start, new_end])

        return ans