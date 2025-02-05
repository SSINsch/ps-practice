class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        num_non_equal = 0
        pair_non_equal = []
        for a, b in zip(s1, s2):
            if a != b:
                num_non_equal = num_non_equal + 1
                pair_non_equal.append((a, b))

        if num_non_equal == 0:
            return True
        elif num_non_equal == 2:
            if (pair_non_equal[0][0] == pair_non_equal[1][1]) and (pair_non_equal[0][1] == pair_non_equal[1][0]):
                return True
            else:
                return False
        else:
            return False