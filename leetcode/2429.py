class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        # get binary form of input integers
        bin1 = format(num1, 'b')
        bin2 = format(num2, 'b')

        # unify length of string
        if len(bin1) > len(bin2):
            bin2 = '0'*(len(bin1)-len(bin2)) + bin2
        else:
            bin1 = '0'*(len(bin2)-len(bin1)) + bin1

        # get number of set bits, but not the index itself, but index with digits
        indices2 = [(len(bin2)-1-i) for i, char in enumerate(bin2) if char == '1']
        num_set2 = len(indices2)
        indices1 = [(len(bin1)-1-i) for i, char in enumerate(bin1) if char == '1']
        num_set1 = len(indices1)

        # find x which satisfies (x XOR num1 is minimal)
        if num_set1 >= num_set2:
            # need to remove (num_set2 bits) starting from the biggest part
            # which means need to use indices until (num_set2)
            ans_indices = indices1[:num_set2]

        else:
            # num_set2 > num_set1
            # need to add all indices in indices 1 => which means add (num_set1) "1"
            # and add (num_set2 - num_set1) "1" from the smallest part
            ans_indices = indices1
            for n in range(len(bin1)):
                if n not in indices1:
                    ans_indices.append(n)
                if len(ans_indices) == num_set2:
                    break

        ans_decimal = 0
        for index in ans_indices:
            ans_decimal = ans_decimal + pow(2, index)

        return ans_decimal


s = Solution()
print(s.minimizeXor(3, 5))
print(s.minimizeXor(1, 12))
print(s.minimizeXor(25, 72))