from collections import Counter
from typing import Union
import string


class Solution:
    @staticmethod
    def _check_add(ans: str, count: Counter) -> bool:
        for c in reversed(string.ascii_lowercase):
            if count[c]:
                return ans[-1] == c
        return False

    @staticmethod
    def _get_char(ans: str, count: Counter) -> Union[int, str]:
        for c in reversed(string.ascii_lowercase):
            if count[c] and (not ans or ans[-1] != c):
                return c
        return -1

    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        ans = ''
        count = Counter(s)

        while True:
            if ans != '':
                flag_add = self._check_add(ans, count)
            else:
                flag_add = False
            c = self._get_char(ans, count)

            if c == -1:
                break

            if flag_add:
                repeats = 1
            else:
                repeats = min(count[c], repeatLimit)

            ans = ans + c * repeats
            count[c] = count[c] - repeats

        return ans


s = Solution()
test_str, test_num = "cczazcc", 3
x = s.repeatLimitedString(test_str, test_num)
print(test_str, x)

test_str, test_num = "cczzccazzcaz", 2
x = s.repeatLimitedString(test_str, test_num)
print(test_str, x)

test_str, test_num = "aababab", 2
x = s.repeatLimitedString(test_str, test_num)
print(test_str, x)

test_str, test_num = "cczzccaaaaaaazzcaz", 2
x = s.repeatLimitedString(test_str, test_num)
print(test_str, x)

test_str, test_num = "a"*20000+'b'*20000, 1
x = s.repeatLimitedString(test_str, test_num)
print(x)
