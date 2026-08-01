"""
Day 6 - Maximum Subarray  (LeetCode #53, Medium)
https://leetcode.com/problems/maximum-subarray/

The task: given an integer array `nums`, find the contiguous subarray with the
largest sum and return that sum. (Subarray = a run of consecutive elements.)

I solved this two ways.

Approach 1 - Brute force:
    I tried every possible subarray. For each start index i, I let the end index j
    run forward, adding nums[j] to a running `current_sum`, and tracked the largest
    sum I ever saw. This checks all O(n^2) subarrays. I started `max_sum` at
    negative infinity so it works even when every number is negative. Time O(n^2),
    space O(1).

Approach 2 - Kadane's Algorithm (optimized):
    The key realisation: as I scan left to right, at each number I only have two
    choices - either extend the subarray I've been building (current_sum + num), or
    start fresh from the current number (num). I take whichever is bigger. If the
    running sum ever goes negative it can only drag the next element down, so
    starting fresh is better - and `max(num, current_sum + num)` captures exactly
    that. I keep `best_sum` as the largest running sum I've seen. That's a single
    O(n) pass with O(1) space.

Approach 2 (Kadane's) is the efficient one - it turns the O(n^2) double loop into
one clean linear scan.
"""


class Solution(object):
    # Approach 1 - Brute force  |  Time: O(n^2)  |  Space: O(1)
    def max_subarray_bruteforce(self, nums):
        max_sum = float('-inf')
        for i in range(len(nums)):
            current_sum = 0
            for j in range(i, len(nums)):
                current_sum += nums[j]
                max_sum = max(max_sum, current_sum)
        return max_sum

    # Approach 2 - Kadane's Algorithm (optimized)  |  Time: O(n)  |  Space: O(1)
    def maxSubArray(self, nums):
        current_sum = nums[0]
        best_sum = nums[0]
        for num in nums[1:]:
            current_sum = max(num, current_sum + num)
            best_sum = max(best_sum, current_sum)
        return best_sum


if __name__ == "__main__":
    sol = Solution()
    print(sol.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # -> 6  (subarray [4,-1,2,1])
    print(sol.maxSubArray([1]))                              # -> 1
    print(sol.maxSubArray([5, 4, -1, 7, 8]))                 # -> 23 (whole array)
