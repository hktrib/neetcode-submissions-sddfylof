class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_count = {}

        for char in s1:
            s1_count[char] = s1_count.get(char, 0) + 1
        
        required = len(s1_count)
        have = 0

        window_count = {}

        l = 0
        for r in range(len(s2)):
            r_char = s2[r]
            window_count[r_char] = window_count.get(r_char, 0) + 1

            if r_char in s1_count and s1_count[r_char] == window_count[r_char]:
                have += 1
            
            # increment left til we get s1 length of window length
            if (r - l + 1) > len(s1):
                l_char = s2[l]
                
                if l_char in s1_count and window_count[l_char] == s1_count[l_char]:
                    have -=1

                window_count[l_char] -= 1
                l += 1
            
            if have == required:
                return True
        return False
                


