class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Basically before replacement we are looking for the
        # longest substring with only k + 1 different characters

        # Such a substring after replacement would be our answer

        res = 0
        l = 0

        # k1_diff = dict()

        s_count = dict()

        length = 0

        maxCountReps = 0

        # x -> 1
        # y -> 1
        # y -> 2

        for r in range(len(s)):

            s_count[s[r]] = 1 + s_count.get(s[r], 0)



            maxCountReps = max(maxCountReps, s_count[s[r]])

            if (r - l + 1) - maxCountReps > k:
                s_count[s[l]] -= 1
                l += 1

        
        return (r - l + 1)
            