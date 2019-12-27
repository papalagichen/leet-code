class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        return -1 if a == b else max(len(a), len(b))


if __name__ == '__main__':
    import Test

    Test.test(Solution().findLUSlength, [
        (("aba", "cdc"), 3),
        (("abc", "abc"), -1),
    ])
