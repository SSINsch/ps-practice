class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        open_indices, mutable_indices = [], []
        size = len(s)

        # odd length => false
        if size % 2 == 1:
            return False

        # get indices of '(' from string s
        # get indices of '0' from string locked
        for i in range(size):
            if locked[i] == '0':
                mutable_indices.append(i)
            elif s[i] == '(':
                open_indices.append(i)
            else:
                if len(open_indices) > 0:
                    pop_item = open_indices.pop()
                elif len(mutable_indices) > 0:
                    pop_item = mutable_indices.pop()
                else:
                    return False

                if pop_item is None:
                    return False

        # pop '(' from open_indices
        # pop ')' from mutable_indices
        # if index of '(' is bigger than ')' => invalid string
        while open_indices and mutable_indices:
            pop_open = open_indices.pop()
            pop_mut = mutable_indices.pop()
            if pop_open > pop_mut:
                return False

        # if there are leftover '(' => invalid string
        if len(open_indices) > 0:
            return False
        else:
            return True


sol = Solution()
print(sol.canBeValid(s="))()))", locked='010100'))
print(sol.canBeValid(s="()()", locked='0000'))
print(sol.canBeValid(s=")", locked='0'))
print(sol.canBeValid(s="())(()(()(())()())(())((())(()())((())))))(((((((())(()))))(",
                     locked='100011110110011011010111100111011101111110000101001101001111'))
print(sol.canBeValid(s="))))(())((()))))((()((((((())())((()))((((())()()))(()",
                     locked="101100101111110000000101000101001010110001110000000101"))