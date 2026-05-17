class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # We can find the smallest element
        # and set it to L
        # We can reverse the logic and find the largest element
        # and set it to R

        # then we can do our basic Binary Search
        # with l
        if len(nums) == 1:
            return -1 if nums[0] != target else 0

        l = 0
        r = len(nums) - 1
        smallest = nums[0]

        print(f"5 + 0 // 2 {(5 + 0) // 2}")

        while l <= r:
            if nums[l] < nums[r]:
                smallest = l if nums[l] < smallest else smallest
                break
            m = ((r + l) // 2)
            smallest = m if nums[m] < smallest else smallest

            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1


        pivot = smallest
        left = 0
        right = len(nums) - 1


        if nums[pivot] == target:
            return pivot
        elif nums[left] > target:
            left = (pivot + 1) % len(nums)
        elif nums[right] < target:
            right = (pivot - 1) % len(nums)

        while left <= right:
            middle = ((left + right)) // 2
            
            if nums[middle] == target:
                return middle
            elif nums[middle] > target:
                right = middle - 1
            else:
                left = middle + 1

        return -1