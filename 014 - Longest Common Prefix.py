class Solution:
    def longestCommonPrefix(self, strs):
        strs = sorted(strs)
        prefix = ''
        if strs:
            for i in range(len(strs[0])):
                if any(strs[0][i] != s[i] for s in strs[1:]):
                    return prefix
                prefix += strs[0][i]
        return prefix


class Solution2:
    def longestCommonPrefix(self, strs):
        prefix = ''
        if strs:
            for i in range(len(strs[0])):
                for s in strs[1:]:
                    if i >= len(s) or strs[0][i] != s[i]:
                        return prefix
                prefix += strs[0][i]
        return prefix


class Solution3:
    def longestCommonPrefix(self, strs):
        if len(strs) == 0:
            return ''
        prefix = strs[0]
        for s in strs:
            i = 0
            while i < len(s) and i < len(prefix) and s[i] == prefix[i]:
                i += 1
            prefix = prefix[:i]
        return prefix


if __name__ == '__main__':
    import Test

    Test.test(Solution().longestCommonPrefix, [
        ((), ''),
        (('1234', '123'), '123'),
        (('1234', '123', '123456', '0', ''), ''),
        (('12345', '123', '123456'), '123'),
        (('12345', '124', '123456'), '12'),
        (('124', '12345', '123456'), '12'),
    ])
    Test.test(Solution2().longestCommonPrefix, [
        ((), ''),
        (('1234', '123'), '123'),
        (('1234', '123', '123456', '0', ''), ''),
        (('12345', '123', '123456'), '123'),
        (('12345', '124', '123456'), '12'),
        (('124', '12345', '123456'), '12'),
    ])
    Test.test(Solution3().longestCommonPrefix, [
        ((), ''),
        (('1234', '123'), '123'),
        (('1234', '123', '123456', '0', ''), ''),
        (('12345', '123', '123456'), '123'),
        (('12345', '124', '123456'), '12'),
        (('124', '12345', '123456'), '12'),
    ])
