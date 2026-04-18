class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = { i:[] for i in range(numCourses)}

        # all courses along curr DFS path
        visitSet = set()

        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        
        def dfs(crs):
            # Hit a loop
            if crs in visitSet:
                return False

            # No prereq, we can take this course!!!
            if preMap[crs] == []:
                return True
            
            visitSet.add(crs)
            for prereq in preMap[crs]:
                if not dfs(prereq):
                    return False
            visitSet.remove(crs)
            return True
        

        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True
            
          