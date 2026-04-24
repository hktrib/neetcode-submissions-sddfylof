class Solution:
    def isPalindrome(self, s: str) -> bool:

        clean = "".join(char.lower() for char in s if char.isalnum())
        n = len(clean)

        def helper(clean, i) -> bool:
            if i == (n // 2):
                return True
            if clean[i] != clean[n - 1 - i]:
                return False
            else:
                return helper(clean, i + 1)

        return helper(clean, 0)
            