"""
Day 9 - Container With Most Water  (LeetCode #11, Medium)
https://leetcode.com/problems/container-with-most-water/

The task: I'm given an array `height` where each value is a vertical line. I have
to pick two lines that, with the x-axis, hold the most water, and return that
maximum area. The container can't be slanted.

My approach - Two pointers:
    The water a pair of lines holds is width * height, where width is the distance
    between them and height is the *shorter* of the two lines (water spills over the
    shorter side). I start with the widest possible container: one pointer at the far
    left, one at the far right.

    At each step I compute the area and update `max_water`. Then I move a pointer
    inward - but which one? Moving inward always shrinks the width, so the only way
    to possibly gain is to get a taller line. The shorter line is the one capping the
    area, so I move the pointer at the shorter line and leave the taller one. If they
    tie it doesn't matter which I move. I keep going until the pointers meet.

    Each line is visited once, so it's a single O(n) pass with O(1) space - much
    better than checking all O(n^2) pairs.
"""


class Solution(object):
    # Two pointers  |  Time: O(n)  |  Space: O(1)
    def maxArea(self, height):
        left = 0
        right = len(height) - 1
        max_water = 0

        while left < right:
            width = right - left
            container_height = min(height[left], height[right])
            area = width * container_height

            max_water = max(max_water, area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_water


if __name__ == "__main__":
    sol = Solution()
    print(sol.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))  # -> 49
    print(sol.maxArea([1, 1]))                        # -> 1
