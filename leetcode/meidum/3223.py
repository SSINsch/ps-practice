from collections import Counter


class Solution:
    def minimumLength(self, s: str) -> int:
        # get alphabet and frequency
        alphabet_counter = Counter(s)

        count = 0
        for al in alphabet_counter:
            # if frequency even, get two middle elements
            if alphabet_counter[al] % 2 == 0:
                count = count + 2
            # if frequency odd, get only middle element
            else:
                count = count + 1

        return count


s = Solution()
print(s.minimumLength("abaacbcbb"))
print(s.minimumLength("aa"))
