class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0

        for i in range(len(heights)):
            start = i
            while stack and heights[i] < stack[-1][1]:
                ind, stHght = stack.pop()
                maxArea = max((i - ind) * stHght, maxArea)
                start = ind

            stack.append((start, heights[i]))
            # maxArea = max(maxArea, heights[i])

        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))

        return maxArea
                