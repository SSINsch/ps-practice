from typing import List


class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        answer = 0
        for i, word_i in enumerate(words):
            for j, word_j in enumerate(words[i+1:]):
                if (word_i == word_j[:len(word_i)]) and (word_i == word_j[-len(word_i):]):
                    answer = answer + 1

        return answer

s = Solution()

words = ["a","aba","ababa","aa"]
print(s.countPrefixSuffixPairs(words))