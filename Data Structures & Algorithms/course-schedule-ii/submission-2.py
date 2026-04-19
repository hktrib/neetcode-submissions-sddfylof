class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # building the Adjacency list
        adj = {}

        for i in range(numCourses):
            adj[i] = []

        for a,b in prerequisites:
            adj[a].append(b)

        # initializing lists/sets        
        res = []

        cycle = set()
        seen = set()

        # dfs
        def dfs(cur):
            # we ended up back at cur in our dfs
            # this means cycle. ERRRROR
            if cur in cycle:
                return False

            # if curr in seen, we can skip. We already checked for a cycle here...
            if cur in seen:
                return True
            
            # add the cycle set to make sure no cycle exists
            cycle.add(cur)

            # check for prereq's that are either
            # in cycle      ->       means we can't do this course
            # or in seen    ->       means no cycle with this node and its dependants
            # and repeat until we get no cycle for all prereqs
            for child in adj[cur]:
                if not dfs(child):
                    return False
            cycle.remove(cur)

            # no cycle add to seen
            seen.add(cur)
            
            # no cycle add to res
            res.append(cur)

            return True
        
        
        for i in range(numCourses):
            # if dfs(i) == false indicates cycle so we can't complete all numCourses
            # return []
            if not dfs(i):
                return []
        
        return res
        



            

