class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Start from the backend and decrement to the front
        # get the current_max temperature and its location
        #       - every decrement increases the distance by one
        #       - every new max resets the distance to one

        stack = [0]
        res = [0] * len(temperatures)

        for i in range(len(temperatures)):
            if i == 0:
                continue
            else:
                while stack != [] and temperatures[stack[-1]] < temperatures[i]:
                    res[stack[-1]] = i - stack[-1]
                    stack.pop()
                
                stack.append(i)
        return res
            

