"""
abc ahbgdc
*   *
 *   *
 *    *
  *    *
  *     *
  *      *

axc ahbgdc
*   *
 *   *
 *    *
 *     *
 *      *
 *       *
"""


# Two Pointer. Time: O(n). Space: O(1)
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False
        return self.helper(s, 0, t, 0)

    def helper(self, s: str, i: int, t: str, j: int) -> bool:
        if i == len(s):
            return True
        if j == len(t):
            return False
        if s[i] == t[j]:
            return self.helper(s, i + 1, t, j + 1)
        else:
            return self.helper(s, i, t, j + 1)


if __name__ == '__main__':
    import Test

    Test.test(Solution().isSubsequence, [
        (("abc", "ahbgdc"), True),
        (("axc", "ahbgdc"), False),
        (("abc", ""), False),
        (("", "ahbgdc"), True),
    ])
