from typing import List


class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        ans = 0
        for item in derived:
            ans = ans ^ item

        if ans == 0:
            return True
        else:
            return False


class SolutionFast:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        return sum(derived) % 2 == 0
