class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_water = 0
        n = len(height)

        start, end = 0, n - 1

        while start < end:

            width = end - start
            ht = min(height[start], height[end])
            current_water = width * ht

            max_water = max(max_water, current_water)

            if height[start] < height[end]:
                start += 1
            else:
                end -= 1

        return max_water
