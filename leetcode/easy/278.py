# The isBadVersion API is already defined for you.
def isBadVersion(version: int) -> bool:
    pass

class Solution:
    def firstBadVersion(self, n: int) -> int:
        cur_left, cur_right = 1, n

        while cur_left < cur_right:
            cursor = (cur_left + cur_right) // 2
            is_bad = isBadVersion(cursor)
            if is_bad:
                cur_right = cursor
            else:
                cur_left = cursor + 1

        return cur_left