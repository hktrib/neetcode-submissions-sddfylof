class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        no_dup = set()

        max_length = 0
        curr_length = 0
        back_ptr = 0

        for i in range(len(s)):
            while s[i] in no_dup:
                no_dup.remove(s[back_ptr])
                back_ptr += 1

            no_dup.add(s[i])
            max_length = max(i - back_ptr + 1, max_length)
        
        return max_length 

                