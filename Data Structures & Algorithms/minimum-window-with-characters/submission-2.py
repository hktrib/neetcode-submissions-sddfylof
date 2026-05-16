class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        t_count = dict()
        w_count = dict()

        for char in t:
            t_count[char] = t_count.get(char, 0) + 1
                
        required = len(t_count)
        have = 0

        res, res_size = [-1, -1], float('inf')
        l = 0

        for r in range(len(s)):
            char_r = s[r]
            w_count[char_r] = w_count.get(char_r, 0) + 1

            if char_r in t_count and w_count[char_r] == t_count[char_r]:
                have += 1

            while have == required:
                if (r - l + 1) < res_size:
                    res_size = (r - l + 1)
                    res = [l, r]

                char_l = s[l]

                if char_l in t_count and w_count[char_l] == t_count[char_l]:
                    have -= 1
                    
                w_count[char_l] = w_count.get(char_l, 0) -1
                
                l += 1

        return "" if res_size == float('inf') else s[res[0] : res[1] + 1]

                
        
