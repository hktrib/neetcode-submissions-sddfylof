class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hmap = dict()

        for c in s:
            if c in hmap:
                hmap[c] += 1
            else:
                hmap[c] = 1
        

        for ch in t:
            if ch in hmap:
                if hmap[ch] == 0:
                    return False
                else:
                    hmap[ch] -= 1
            else:
                print("returned from else")
                return False
        
        print("returned from sum")
        
        total = sum(hmap.values())

        return total == 0

