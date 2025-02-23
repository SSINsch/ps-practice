from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dictionary = Counter(magazine)
        target = Counter(ransomNote)

        for alphabet in target:
            if target[alphabet] > dictionary[alphabet]:
                return False

        return True
