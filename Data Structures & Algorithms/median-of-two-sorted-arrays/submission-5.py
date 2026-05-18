class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # m = len(nums1)
        # n = len(nums2)


        A, B = nums1, nums2
        total = len(A) + len(B)
        half = total // 2

        if len(A) > len(B):
            A, B = B, A

        l, r = 0, len(A) - 1

        while True:
            i = (l + r) // 2
            j = half - i - 2

            # If i is negative, there is nothing from A on the left side
            Aleft = A[i] if i >= 0 else float("-infinity")
            # If i + 1 is past the end of A, there is nothing from A on the right side
            Aright = A[i + 1] if (i + 1) < len(A) else float("infinity")

            # If j is negative, there is nothing from B on the left side
            Bleft = B[j] if j >= 0 else float("-infinity")
            # If j + 1 is past the end of B, there is nothing from B on the right side
            Bright = B[j + 1] if (j + 1) < len(B) else float("infinity")

            if Aleft <= Bright and Bleft <= Aright:
                if total % 2:
                    return min(Aright, Bright)
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:
                r = i - 1
            else:
                l = i + 1

        # Either m + n is odd
        # or m + n is even
        

        # if m + n is odd, we get our (m + n + 1) / 2
        # 