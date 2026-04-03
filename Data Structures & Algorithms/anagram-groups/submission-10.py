class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        anagrammed = dict()

        for i, s in enumerate(strs):
            if i in anagrammed:
                continue
            else:
                anagramList = [s]
                anagrammed[i] = 1
                
                for j, t in enumerate(strs):
                    if i == j or len(s) != len(t) or j in anagrammed:
                        continue
                    else:
                        if self.isAnagram(s, t):
                            anagrammed[j] = 1
                            anagramList.append(t)
                
                res.append(anagramList)

        return res
                
    def isAnagram(self, s: str, t: str) -> bool:
        # if len(s) != len(t):
        #     return False
        if len(s) == 0:
            return True
        
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
        
        # for val in hashmap.values():
        #     if val != 0:
        #         return False

        return True
            

