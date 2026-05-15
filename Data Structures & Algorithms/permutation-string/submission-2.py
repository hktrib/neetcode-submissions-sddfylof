class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        m = {}
        total = 0
        for s in s1:
            m[s] = m.get(s, 0) + 1
            total += 1
        
        print(f"total: {total} | m{m}")

        k = len(s1)
        l = 0
        r = 0
        while r < len(s2):
            if s2[r] not in m:
                # skip
                r += 1
                while l < r:
                    if s2[l] in m:
                        m[s2[l]] += 1
                        total += 1
                    l += 1
            else: 
                if m[s2[r]] > 0:
                    m[s2[r]] -= 1
                    total -= 1
                    r += 1
                else: 
                    if s2[l] in m:
                        m[s2[l]] += 1
                        total += 1
                    l += 1

            if total == 0:
                return True

        
        return False