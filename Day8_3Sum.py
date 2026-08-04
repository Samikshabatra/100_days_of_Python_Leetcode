"""
Day 8 - 3Sum  (LeetCode #15, Medium)
https://leetcode.com/problems/3sum/

The task: given an integer array `nums`, return all unique triplets
[nums[i], nums[j], nums[k]] with i, j, k all different that add up to 0. The
result must not contain duplicate triplets.

My approach - Brute force (three nested loops):
    I picked every possible combination of three different indices i < j < k and
    checked whether nums[i] + nums[j] + nums[k] == 0. When a triplet summed to zero
    I sorted it (so [-1, 0, 1] and [0, -1, 1] look the same) and only added it if it
    wasn't already in `result`, which handles the "no duplicates" rule.

    This is correct, but it's O(n^3) from the three loops, and the `triplet not in
    result` check adds even more work. On LeetCode it passed 311/316 test cases and
    then hit **Time Limit Exceeded** on the large inputs - so it's right in logic but
    too slow to accept. Keeping it here as my honest first attempt.

    Time O(n^3). Space O(1) beyond the output.

Next step (optimization I want to do): sort nums first, fix one number, and use a
two-pointer scan on the rest to bring it down to O(n^2). Not implemented yet.
"""


class Solution(object):
    # Brute force - three nested loops  |  Time: O(n^3)  |  Space: O(1) extra
    # NOTE: correct but Time Limit Exceeded on large inputs (311/316 on LeetCode).
    def threeSum(self, nums):
        result = []
        n = len(nums)
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                for k in range(j + 1, n):
                    if nums[i] + nums[j] + nums[k] == 0:
                        triplet = sorted([nums[i], nums[j], nums[k]])
                        if triplet not in result:
                            result.append(triplet)
        return result


if __name__ == "__main__":
    sol = Solution()
    print(sol.threeSum([-1, 0, 1, 2, -1, -4]))  # -> [[-1, -1, 2], [-1, 0, 1]]
    print(sol.threeSum([0, 1, 1]))               # -> []
    print(sol.threeSum([0, 0, 0]))               # -> [[0, 0, 0]]
