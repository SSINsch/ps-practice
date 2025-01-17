from typing import List


class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        set_a = set()
        set_b = set()
        size = len(A)
        ans = []
        count = 0

        for i in range(size):
            set_a.add(A[i])
            set_b.add(B[i])

            # if the i-th element same, increase 1
            if A[i] == B[i]:
                count = count + 1

            # if the i-th element different, need to check if items are already included
            else:
                if A[i] in set_b:
                    count = count + 1
                if B[i] in set_a:
                    count = count + 1
            ans.append(count)

        return ans

s = Solution()
print(s.findThePrefixCommonArray([1,3,2,4], [3,1,2,4]))