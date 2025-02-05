class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open_character = ['(', '{', '[']
        close_character = [')', '}', ']']
        pair = {k: v for k, v in zip(open_character, close_character)}

        if len(s) % 2 == 1:
            return False

        for idx, c in enumerate(s):
            if c in open_character:
                stack.append(c)
            elif c in close_character:
                try:
                    top = stack.pop()
                except IndexError as ie_error:
                    return False
                if c != pair[top]:
                    return False
            else:
                raise ValueError('invalid character')

        if len(stack) > 0:
            return False

        return True

s = Solution()
print(s.isValid('(){}}{'))