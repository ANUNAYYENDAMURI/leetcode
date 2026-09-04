class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:

            mid = (left + right) // 2

            if nums[mid] < nums[mid + 1]:
                # We are on the increasing side
                left = mid + 1
            else:
                # We are on the decreasing side
                right = mid

        return left