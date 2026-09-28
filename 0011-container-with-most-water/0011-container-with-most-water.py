class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        maximum = 0

        while l < r:
            width = r - l
            min_height = min(height[l], height[r])

            area = width * min_height
            maximum = max(maximum, area)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return maximum