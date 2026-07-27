"""
Day 5 - Valid Parentheses  (LeetCode #20, Easy)
https://leetcode.com/problems/valid-parentheses/

The task: given a string `s` of just the brackets ()[]{}, decide if it's valid.
Valid means every opening bracket is closed by the same type, in the correct
order, and every closing bracket has a matching opener.

My approach - Stack:
    Brackets have to close in reverse order of how they opened - the most recent
    unclosed opener is the first one that needs to be matched. That "last in, first
    out" behaviour is exactly a stack, so I used one.

    I keep a `pairs` map from each closing bracket to the opening bracket it needs.
    Then I walk the string:
      - If the character is an opener, I push it onto the stack.
      - If it's a closer, I check the stack. If it's empty there's nothing to match,
        so it's invalid. Otherwise I pop the top opener and make sure it matches the
        closer via `pairs` - if it doesn't, the order is wrong and it's invalid.
    At the end, a valid string leaves the stack empty (every opener got closed).
    If anything is left over, some brackets were never closed, so I return False.

    Each character is pushed/popped at most once, so it's a single O(n) pass.
    Space is O(n) for the stack in the worst case (a string of all openers).
"""


class Solution(object):
    # Stack  |  Time: O(n)  |  Space: O(n)
    def isValid(self, s):
        stack = []
        pairs = {
            ')': '(',
            ']': '[',
            '}': '{',
        }
        for ch in s:
            if ch in "([{":
                stack.append(ch)
            else:
                if not stack:
                    return False
                top = stack.pop()
                if top != pairs[ch]:
                    return False
        return len(stack) == 0


if __name__ == "__main__":
    sol = Solution()
    print(sol.isValid("()"))        # -> True
    print(sol.isValid("()[]{}"))    # -> True
    print(sol.isValid("(]"))        # -> False
    print(sol.isValid("([)]"))      # -> False (wrong order)
    print(sol.isValid("("))         # -> False (never closed)
