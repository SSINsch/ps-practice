class Solution:
    def climbStairs(self, n: int) -> int:
        fibonacci = [1, 1, 2]

        for i in range(3, n + 1):
            fibonacci.append(fibonacci[i - 1] + fibonacci[i - 2])

        return fibonacci[n]