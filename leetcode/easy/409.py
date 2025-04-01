from collections import Counter


class Solution:
    def longestPalindrome(self, s: str) -> int:
        dict_s = Counter(s)
        max_length, flag_odd = 0, False
        print(dict_s)

        for k in dict_s:
            # if even, just add
            if dict_s[k] % 2 == 0:
                max_length = max_length + dict_s[k]
            # if odd, find the largest number
            else:
                flag_odd = True
                max_length = max_length + dict_s[k] - 1

        if flag_odd:
            max_length = max_length + 1

        return max_length