"""
Day 1 - Two Sum  (LeetCode #1, Easy)
https://leetcode.com/problems/two-sum/

The task: given an array `nums` and an integer `target`, return the indices of
the two numbers that add up to the target.

I solved this two ways.

Approach 1 - Brute force (my first attempt):
    I checked every possible pair of numbers using a nested loop and returned the
    pair whose sum matched the target. It works, but for every element I re-scan
    the rest of the array, so it costs O(n^2) time. Space is O(1).

Approach 2 - Hash map (my optimized solution):
    I realized I don't need to compare every pair - I only need to know whether the
    "missing piece" of a number has already shown up. So I walk the array once, and
    for each number I compute complement = target - num. If I've already seen that
    complement, I've found my answer. Otherwise I store the current number with its
    index and keep going. Dictionary lookups are O(1), so this runs in a single
    O(n) pass. Space is O(n) for the dictionary.

Approach 2 is the one I'd submit - same correct result, much faster on large inputs.
"""


class Solution(object):
    # Approach 1 - Brute force  |  Time: O(n^2)  |  Space: O(1)
    def two_sum_bruteforce(self, nums, target):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []

    # Approach 2 - Hash map (optimized)  |  Time: O(n)  |  Space: O(n)
    def twoSum(self, nums, target):
        seen = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in seen:
                return [seen[complement], i]
            seen[nums[i]] = i
        return []


if __name__ == "__main__":
    sol = Solution()
    print(sol.twoSum([2, 7, 11, 15], 9))  # -> [0, 1]
    print(sol.twoSum([3, 2, 4], 6))        # -> [1, 2]
    print(sol.twoSum([3, 3], 6))           # -> [0, 1]
