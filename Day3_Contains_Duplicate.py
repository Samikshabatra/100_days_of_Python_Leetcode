"""
Day 3 - Contains Duplicate  (LeetCode #217, Easy)
https://leetcode.com/problems/contains-duplicate/

The task: given an integer array `nums`, return True if any value appears at
least twice, and False if every element is distinct.

My approach - Hash set (one pass):
    The naive idea would be to compare every element with every other one and
    check for a match, but that's a nested loop = O(n^2) time. Instead, I kept a
    `seen` set and walked the array once. For each number I first check if it's
    already in `seen` - if it is, I've found a duplicate and return True right
    away. Otherwise I add it to the set and move on. If I get through the whole
    array without a repeat, everything was distinct, so I return False.

    Because set membership checks and inserts are O(1) on average, the whole thing
    is a single O(n) pass. Space is O(n) for the set in the worst case (all
    elements distinct).
"""


class Solution(object):
    # Hash set (one pass)  |  Time: O(n)  |  Space: O(n)
    def containsDuplicate(self, nums):
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False


if __name__ == "__main__":
    sol = Solution()
    print(sol.containsDuplicate([1, 2, 3, 1]))                    # -> True  (1 repeats)
    print(sol.containsDuplicate([1, 2, 3, 4]))                    # -> False (all distinct)
    print(sol.containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))  # -> True
