class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Memoization with Dict solution!!!!!
        n = len(s)
        if n < 2:
            return s
            
        res = s[0]
        resLen = 1
        memo = [[None for _ in range(n)] for _ in range(n)]
        

        def checkPalindrome(i, j):
            if i == j:
                return True
            elif i + 1 == j:
                return s[i] == s[j]
            elif memo[i][j] is not None:
                return memo[i][j]
            else:
                # Recursive Step: 
                # S[i..j] is a palindrome 
                #   ONLY IF outer chars match 
                #   AND the inner substring S[i+1..j-1] is a palindrome.
                memo[i][j] = s[i] == s[j] and checkPalindrome(i + 1, j - 1)
                return memo[i][j]
        

        for i in range(len(s)):
            for j in range(i, len(s)):
                if checkPalindrome(i, j):
                    if resLen < (j - i + 1):
                        resLen = j - i + 1
                        res = s[i: j + 1]

        return res