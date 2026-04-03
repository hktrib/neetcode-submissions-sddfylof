class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hs = set()
        l = 0

        res = 0
        for r in range(len(s)):
            if s[r] in hs:
                while s[r] in hs:
                    print(f"s[r] {s[r]} | Hashset {hs} | l = {l}")
                    hs.remove(s[l])
                    l += 1
            hs.add(s[r])
            res = max(res, len(hs))

        return res


