class Solution:
    def countSubstrings(self, s: str) -> int:
        
        n = len(s)
        # Initially every caharacter by itself should be a palindrome
        count = n

        memo = [[None for _ in range(n)] for _ in range(n)]

        def checkPalindrome(i, j):
            if i == j:
                return True
            elif i + 1 == j:
                return s[i] == s[j]
            elif memo[i][j] is not None:
                return memo[i][j]
            else:

                memo[i][j] = s[i] == s[j] and checkPalindrome(i + 1, j - 1)
                return memo[i][j]


        for i in range(n):
            for j in range(i + 1, n):
                if checkPalindrome(i, j):
                    count += 1
        
        return count