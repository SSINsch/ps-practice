class Solution:
    def addBinary(self, a: str, b: str) -> str:
        decimal_a = int(a, 2)
        decimal_b = int(b, 2)

        binary_str = bin(decimal_a + decimal_b)[2:]

        return binary_str
