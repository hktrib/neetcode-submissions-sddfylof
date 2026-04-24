class Solution:
    def isPalindrome(self, s: str) -> bool:

        s = "".join(char.lower() for char in s if char.isalnum())
        n = len(s)

        def helper(s, i) -> bool:
            if i == (n // 2):
                return True
            if s[i] != s[n - 1 - i]:
                return False
            else:
                return helper(s, i + 1)

        return helper(s, 0)
            