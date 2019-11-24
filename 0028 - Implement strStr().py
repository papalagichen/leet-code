class Solution:
    def strStr(self, haystack, needle):
        n = len(needle)
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i + n] == needle:
                return i
        return -1


if __name__ == '__main__':
    import Test

    Test.test(Solution().strStr, [
        (('22123123', '123'), 2),
        (('', '123'), -1),
        (('', ''), 0),
        (('123', '123'), 0),
    ], copy_parameters=False)
