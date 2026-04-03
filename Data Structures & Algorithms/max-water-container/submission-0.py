class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # if len(heights) <= 1:
        #     return 0

        area = 0

        for i in range(len(heights)):
            for j in range(i + 1, len(heights)):
                print()
                res = (j - i) * min(heights[i], heights[j]) 
                if area <= res:
                    area = res


        # left = 0
        # right = len(heights) - 1




        # while right < left:
        #     if heights[right] < heights[right - 1]:
        #         right -= 1
        #     elif heights[left] < heights[left + 1]:
        #         left += 1
        #     else:
        #         break
        
        # return (right - left) * min(heights[left], heights[right])
        return area
        pass