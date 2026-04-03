class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        
        dup = set()

        maxLength = 0

        maxString = ""
        string = ""

        for r in range(len(s)):
            while s[r] in dup:
                dup.remove(s[l])
                string = string[1:]
                l += 1
            
            string += s[r]
            dup.add(s[r])

            maxLength = max(maxLength, (r - l + 1))
            maxString = maxString if maxString > string else string

        print(f"MaxString: {maxString}")

        return maxLength


       

                