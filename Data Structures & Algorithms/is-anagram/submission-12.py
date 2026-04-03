class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap = dict()

        
        for c in s:
            if c not in hashmap:
                hashmap[c] = 1
            else:
                hashmap[c] += 1

        for ch in t:
            if ch not in hashmap or hashmap[ch] == 0:
                return False
            else:
                hashmap[ch] -= 1

        for val in hashmap.values():
            if val != 0:
                return False

        return True

