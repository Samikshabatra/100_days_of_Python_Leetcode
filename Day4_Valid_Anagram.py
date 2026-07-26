"""
Day 4 - Valid Anagram  (LeetCode #242, Easy)
https://leetcode.com/problems/valid-anagram/

The task: given two strings `s` and `t`, return True if `t` is an anagram of `s`
(same letters, same counts, just reordered) and False otherwise.

I solved this two ways.

Approach 1 - Sorting:
    If two strings are anagrams they must have the exact same characters, so once
    I sort both of them they should come out identical. I first do a quick length
    check (different lengths can't be anagrams), then just compare sorted(s) with
    sorted(t). It's short and clean, but sorting costs O(n log n) time.

Approach 2 - Hash map (counting letters):
    I don't actually need to sort - I only need to know that every letter appears
    the same number of times in both strings. So I count each character of `s` in a
    dictionary, then walk through `t` decrementing those counts. If I hit a letter
    that isn't in the map, or a count drops below zero, `t` has a letter `s` doesn't
    (or too many of one), so it's not an anagram. If I get through cleanly, they
    match. Counting is a single pass each way: O(n) time, O(1) space since there are
    only 26 lowercase letters.

Approach 2 is the faster one - it turns the O(n log n) sort into an O(n) count.
"""


class Solution(object):
    # Approach 1 - Sorting  |  Time: O(n log n)  |  Space: O(n)
    def is_anagram_sorting(self, s, t):
        if len(s) != len(t):
            return False
        return sorted(s) == sorted(t)

    # Approach 2 - Hash map / letter counts  |  Time: O(n)  |  Space: O(1)
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        count = {}
        for ch in s:
            count[ch] = count.get(ch, 0) + 1
        for ch in t:
            if ch not in count:
                return False
            count[ch] -= 1
            if count[ch] < 0:
                return False
        return True


if __name__ == "__main__":
    sol = Solution()
    print(sol.isAnagram("anagram", "nagaram"))  # -> True
    print(sol.isAnagram("rat", "car"))          # -> False
