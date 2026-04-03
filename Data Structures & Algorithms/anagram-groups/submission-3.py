class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        processed = [False] * len(strs)

        for i, s in enumerate(strs):
            if processed[i]:
                continue
            anagramList = [s]
            processed[i] = True
            
            for j, t in enumerate(strs):
                if processed[j] or i == j or len(s) != len(t):
                    continue
                if self.isAnagram(s, t):
                    processed[j] = True
                    anagramList.append(t)
            
            res.append(anagramList)
        return res
                
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
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
        
        return True

