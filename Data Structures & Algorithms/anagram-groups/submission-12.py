class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:


        # Solution #1: Brute Force -> Time Complexity (O(N^2 * K) with K being max length of a word)
        # Note: The reason why we can't use the String itself as the Key in the
        # dictionary keeping track of what has been processed is that, our purpose
        # is not to skip over a duplicate word, But to also concatenate that word
        # into our running list of anagrams of that particular combination.
        # res = []
        # anagrammed = dict()

        # for i, s in enumerate(strs):
        #     if i in anagrammed:
        #         continue
        #     else:
        #         anagramList = [s]
        #         anagrammed[i] = 1
                
        #         for j, t in enumerate(strs):
        #             if i == j or len(s) != len(t) or j in anagrammed:
        #                 continue
        #             else:
        #                 if self.isAnagram(s, t):
        #                     anagrammed[j] = 1
        #                     anagramList.append(t)
                
        #         res.append(anagramList)

        # return res


        hm = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            
            # print(f"s = {s} | [s] = {[s]}")
            hm[tuple(count)].append(s)
        
        return list(hm.values())

                
    def isAnagram(self, s: str, t: str) -> bool:
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
            

