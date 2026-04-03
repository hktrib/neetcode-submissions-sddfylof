class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # if len(heights) <= 1:
        #     return 0

        # area = 0

        # for i in range(len(heights)):
        #     for j in range(i + 1, len(heights)):
        #         res = (j - i) * min(heights[i], heights[j]) 
        #         if area <= res:
        #             area = res

        area = 0

        l, r = 0, len(heights) - 1

        while l < r:
            res = (r - l) * min(heights[l], heights[r])
            if area <= res:
                area = res


            if heights[l] >= heights[r]:
                r -= 1
            elif heights[l] < heights[r]:
                l += 1
                


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