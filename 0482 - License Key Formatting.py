class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        alphanum = S.replace('-', '').upper()
        length = len(alphanum)
        c = length % K
        if c == 0:
            c = K
        key = alphanum[:c]
        while c < length:
            key += '-' + alphanum[c:c + K]
            c += K
        return key


if __name__ == '__main__':
    import Test

    Test.test(Solution().licenseKeyFormatting, [
        (('2-4A0r7-4k', 4), '24A0-R74K'),
        (('2-4A0r7-4k', 3), '24-A0R-74K'),
        (('2-4A0r7-4k', 2), '24-A0-R7-4K'),
        (('2-4A', 4), '24A'),
    ])
