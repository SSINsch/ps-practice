class Solution:
    @staticmethod
    def clean_and_lowercase(s: str) -> str:
        return ''.join(char.lower() for char in s if char.isalnum())

    def isPalindrome(self, s: str) -> bool:
        cleaned_s = self.clean_and_lowercase(s)
        for i in range(len(cleaned_s)//2):
            if cleaned_s[i] != cleaned_s[len(cleaned_s)-i-1]:
                return False

        return True
