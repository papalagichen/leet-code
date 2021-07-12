from functools import lru_cache
from typing import List

"""
aab => (a, a, b), (aa, b), (a, ab)x, (aab)x
aaba => (a, aba), (a, ab, a)x, (a, a, ba)x, (a, a, b, a), (aa, ba)x, (aa, b, a)
"""


# Backtracking. Time: O(n * 2^n). Space: O(n^2)
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        return self.helper(s, 0, len(s))

    def helper(self, s: str, start: int, end: int) -> List[List[str]]:
        results = []
        if start == end:
            return results
        if self.is_palindrome(s, start, end):
            results.append([s[start:end]])
        for i in range(start, end):
            if self.is_palindrome(s, start, i + 1):
                results.extend([(s[start:i + 1])] + x for x in self.helper(s, i + 1, end))
        return results

    def is_palindrome(self, s: str, start: int, end: int) -> bool:
        while start < end:
            if s[start] != s[end - 1]:
                return False
            start += 1
            end -= 1
        return True


# Dynamic Programming. Time: O(n * 2^n). Space: O(n^2)
class Solution2:
    def __init__(self):
        self.dp = []

    def partition(self, s: str) -> List[List[str]]:
        self.dp = [[None] * (len(s) + 1) for _ in range(len(s) + 1)]
        return self.helper(s, 0, len(s))

    def helper(self, s: str, start: int, end: int) -> List[List[str]]:
        results = []
        if start == end:
            return results
        if self.is_palindrome(s, start, end):
            results.append([s[start:end]])
        for i in range(start, end):
            if self.is_palindrome(s, start, i + 1):
                results.extend([(s[start:i + 1])] + x for x in self.helper(s, i + 1, end))
        return results

    def is_palindrome(self, s: str, start: int, end: int) -> bool:
        if self.dp[start][end] is not None:
            return self.dp[start][end]
        if start >= end - 1:
            result = True
        elif s[start] == s[end - 1]:
            result = self.is_palindrome(s, start + 1, end - 1)
        else:
            result = False
        self.dp[start][end] = result
        return self.dp[start][end]


# Dynamic Programming. Time: O(n * 2^n). Space: O(n^2)
class Solution3:
    def partition(self, s: str) -> List[List[str]]:
        return self.helper(s, 0, len(s))

    def helper(self, s: str, start: int, end: int) -> List[List[str]]:
        results = []
        if start == end:
            return results
        if self.is_palindrome(s, start, end):
            results.append([s[start:end]])
        for i in range(start, end):
            if self.is_palindrome(s, start, i + 1):
                results.extend([(s[start:i + 1])] + x for x in self.helper(s, i + 1, end))
        return results

    @lru_cache()
    def is_palindrome(self, s: str, start: int, end: int) -> bool:
        if start >= end - 1:
            return True
        if s[start] != s[end - 1]:
            return False
        return self.is_palindrome(s, start + 1, end - 1)


# Backtracking. Time: O(n * 2^n). Space: O(n^2)
class Solution4:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        self.dfs(s, [], res)
        return res

    def dfs(self, s, path, res):
        if not s:
            res.append(path)
            return
        for i in range(1, len(s) + 1):
            if self.is_palindrome(s[:i]):
                self.dfs(s[i:], path + [s[:i]], res)

    def is_palindrome(self, s):
        return s == s[::-1]


if __name__ == "__main__":
    import Test

    Test.test([Solution().partition, Solution2().partition, Solution3().partition], [
        ("aab", [["a", "a", "b"], ["aa", "b"]]),
        ("aaa", [["a", "a", "a"], ["a", "aa"], ["aa", "a"], ["aaa"]]),
        ("a", [["a"]]),
        ("aaba", [["a", "a", "b", "a"], ["a", "aba"], ["aa", "b", "a"]]),
    ], sort_result=True)
