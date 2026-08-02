"""
Day 7 - Product of Array Except Self  (LeetCode #238, Medium)
https://leetcode.com/problems/product-of-array-except-self/

The task: given an integer array `nums`, return an array `answer` where answer[i]
is the product of every element except nums[i]. I have to do it in O(n) time and
without using division.

My approach - Prefix and suffix products:
    The product of everything except nums[i] is just (product of everything to its
    left) times (product of everything to its right). So I build two helper arrays:
      - left[i]  = product of all elements before index i
      - right[i] = product of all elements after index i
    left is filled going forward (each entry is the previous left times the previous
    number), and right is filled going backward the same way. Then answer[i] is
    simply left[i] * right[i]. No division needed, and it's three linear passes, so
    O(n) time.

    (Note to self: on my first try I got an IndexError because I used the wrong loop
    variable while filling `right` - I wrote right[i] = right[i+1] * nums[i+1] inside
    a loop over `j`. Fixed it to use `j` consistently: right[j] = right[j+1] * nums[j+1].)

    Time O(n). Space O(n) for the left/right arrays (the answer array itself doesn't
    count as extra space).
"""


class Solution(object):
    # Prefix + suffix products  |  Time: O(n)  |  Space: O(n)
    def productExceptSelf(self, nums):
        n = len(nums)

        left = [1] * n
        right = [1] * n
        answer = [1] * n

        # left[i] = product of everything before i
        for i in range(1, n):
            left[i] = left[i - 1] * nums[i - 1]

        # right[j] = product of everything after j
        for j in range(n - 2, -1, -1):
            right[j] = right[j + 1] * nums[j + 1]

        for i in range(n):
            answer[i] = left[i] * right[i]

        return answer


if __name__ == "__main__":
    sol = Solution()
    print(sol.productExceptSelf([1, 2, 3, 4]))       # -> [24, 12, 8, 6]
    print(sol.productExceptSelf([-1, 1, 0, -3, 3]))  # -> [0, 0, 9, 0, 0]
