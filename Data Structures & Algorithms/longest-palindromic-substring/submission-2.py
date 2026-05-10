class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        # Basically get all substrings
        # check if they are palindrome 
        # get max Size Palindrome substring

        # Key is to see if the palindromes build upon each other
        # a is a palindrome
        # ab is not 
        # aba is


        # Brute Force recursive

        n = len(s)
        if n < 2:
            return s



        res = s[0]
        resLen = 1
        # abbc

        # start at a
        # abbc

        memo = [[None for _ in range(n)] for _ in range(n)]

        def checkPalindrome(i, j):
            if i == j:
                return True
            elif memo[i][j] is not None:
                return memo[i][j]
            elif i + 1 == j:
                return s[i] == s[j]
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
        # for i in range(len(s)):
        #     for j in range(i, len(s)):
        #         l, r = i, j

        #         # wait until some separation

        #         while l < r and s[l] == s[r]:
        #             l += 1
        #             r -= 1
                
        #         if l >= r and resLen < (j - i + 1):
        #             res = s[i : j + 1]
        #             resLen = j - i + 
