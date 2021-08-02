from functools import lru_cache

"""
a b c
- - - 3
      3

a a a
- - - 3
---   1
  --- 1
----- 1
      6

a b c b a
- - - - - 5
  -----
---------


Two ways to grow the palindrom
a -> a
a <- b -> a
"""


# Brute Force. Time: O(n! * n). Space: O(1)
class Solution:
    def countSubstrings(self, s: str) -> int:
        substr_count = 0
        for i in range(len(s)):
            for length in range(1, len(s) + 1):
                if i + length > len(s):
                    break
                if self.is_palindrom(s, i, i + length - 1):
                    substr_count += 1
        return substr_count

    def is_palindrom(self, s: str, start: int, end: int) -> bool:
        while start < end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
        return True


# Dynamic Programming. Time: O(n!). Space: O(n^2)
class Solution2:
    def countSubstrings(self, s: str) -> int:
        if len(set(s)) == 1:
            return (1 + len(s)) * len(s) // 2
        substr_count = 0
        for i in range(len(s)):
            for length in range(1, len(s) + 1):
                if i + length > len(s):
                    break
                if self.is_palindrom(s, i, i + length - 1):
                    substr_count += 1
        return substr_count

    @lru_cache()
    def is_palindrom(self, s: str, start: int, end: int) -> bool:
        if start >= end:
            return True
        if s[start] != s[end]:
            return False
        return self.is_palindrom(s, start + 1, end - 1)


if __name__ == '__main__':
    import Test

    Test.test([Solution().countSubstrings, Solution2().countSubstrings], [
        ("abc", 3),
        ("aaa", 6),
    ])
