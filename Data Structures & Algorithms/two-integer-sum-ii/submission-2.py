class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        left = 0
        right = len(numbers) - 1

        while left < right:
            lr_sum = numbers[left] + numbers[right]
            if lr_sum == target:
                break

            elif lr_sum > target:
                right -= 1
            else:
                left += 1
        
        return [left + 1 , right + 1]