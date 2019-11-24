class Solution:
    def compareVersion(self, version1, version2):
        version1 = map(int, version1.split('.'))
        version2 = map(int, version2.split('.'))
        for i in range(max(len(version1), len(version2))):
            v1 = version1[i] if i < len(version1) else 0
            v2 = version2[i] if i < len(version2) else 0
            if v1 != v2:
                return cmp(v1, v2)
        return 0

if __name__ == '__main__':
    import Test

    Test.test(Solution().compareVersion, [
        (('0.1', '1.1'), -1),
        (('1.0', '1.0'), 0),
        (('1.0', '0.1'), 1),
        (('1.0.0', '0.0.1'), 1),
        (('01', '1'), 0),
        (('1.0', '1'), 0),
        (('1.1', '1.10'), -1),
    ])
