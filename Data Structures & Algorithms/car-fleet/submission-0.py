class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
            

            us_ps_pairs = list(zip(position, speed))
            
            ps_pairs = sorted(us_ps_pairs, key=lambda x: x[0])
            

            stack = []

            for index in range(len(ps_pairs) - 1, -1, -1):
                if stack == []:
                    stack.append(ps_pairs[index])
                else:
                    top_time = (target - stack[-1][0]) / stack[-1][1] 
                    new_time = (target - ps_pairs[index][0]) / ps_pairs[index][1]

                    if new_time <= top_time:
                        continue
                    else:
                        stack.append(ps_pairs[index])

            print(stack)
            return len(stack)
            pass
