# Two pointers. Time: O(n). Space: O(1)
class Solution:
    def validPalindrome(self, s: str) -> bool:
        return self.helper(s, 0, len(s) - 1, False)

    def helper(self, s: str, i: int, j: int, skipped: bool) -> bool:
        while i <= j:
            if s[i] == s[j]:
                i, j = i + 1, j - 1
            else:
                break
        else:
            return True
        if skipped:
            return False
        return self.helper(s, i + 1, j, True) or self.helper(s, i, j - 1, True)


if __name__ == '__main__':
    import Test

    Test.test(Solution().validPalindrome, [
        ("aba", True),
        ("abca", True),
        ("abcd", False),
        ("a", True),
        ("ab", True),
        ("aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga", True),
    ])
