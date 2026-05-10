class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Memoization with Dict solution!!!!!

        n = len(s)
        if n < 2:
            return s
            
        res = s[0]
        resLen = 1
        memo = defaultdict()
        

        def checkPalindrome(i, j):
            if i == j:
                return True
            elif i + 1 == j:
                return s[i] == s[j]
            elif (i, j) in memo:
                return memo[(i, j)]
            else:
                # Recursive Step: 
                # S[i..j] is a palindrome 
                #   ONLY IF outer chars match 
                #   AND the inner substring S[i+1..j-1] is a palindrome.
                found = s[i] == s[j] and checkPalindrome(i + 1, j - 1)
                memo[(i, j)] = found
                return memo[(i, j)]
        

        for i in range(len(s)):
            for j in range(i + 1, len(s)):
                if checkPalindrome(i, j):
                    if resLen < (j - i + 1):
                        resLen = j - i + 1
                        res = s[i: j + 1]

        return res