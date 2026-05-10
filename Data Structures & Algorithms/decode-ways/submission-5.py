class Solution:
    def numDecodings(self, s: str) -> int:
        # mapping = {}
        # for i in range(26):
        #     mapping[chr(ord('a') + i)] = i + 1

        num_ways = 0
        
        # int(x[0]) == 0 ret false
        # x > 26 ret false

        memo = [-1] * len(s)

        def helper(i):
            if i >= len(s):
                return 1
            elif int(s[i]) == 0:
                return 0
            elif memo[i] != -1:
                return memo[i]
            else:
                # first digit must be 1-9 now
                takeOne = helper(i+1)

                '''
                    i = 0 + 1 < 2 and 


                '''
                takeTwo = 0
                if i+1 < len(s) and int(s[i:i+2]) <= 26:
                    takeTwo = helper(i+2)

                memo[i] = takeOne + takeTwo
                return memo[i]

        num_ways = helper(0)

        return num_ways

