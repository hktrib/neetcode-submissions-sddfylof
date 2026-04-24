class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # create adjacency List

        # need to find one-letter difference

        if endWord not in wordList:
            return 0

        adj = defaultdict(list)



        '''
            bat
                *at
                b*t
                ba*
            

        '''

        wordList.append(beginWord)

        for word in wordList:
            for i in range(len(word)):
                temp = word[0:i] + "*" + word[i + 1:]
                adj[temp].append(word)
        
        
        visited = set([beginWord])
        q = deque([beginWord])
        res = 1

        while q:
            # Go LAYER BY LAYER
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res
                else:
                    for i in range(len(word)):
                        temp = word[0:i] + "*" + word[i + 1:]
                        for neighbor in adj[temp]:
                            if neighbor not in visited:
                                visited.add(neighbor)
                                q.append(neighbor)
            res += 1

        return 0