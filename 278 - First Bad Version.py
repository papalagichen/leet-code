def isBadVersion(version):
    return version > 0


class Solution(object):
    def firstBadVersion(self, n):
        start, end = 1, n
        while True:
            middle = (start + end) / 2
            if isBadVersion(middle):
                if middle == 1 or not isBadVersion(middle - 1):
                    return middle
                end = middle
            else:
                if end - start == 1:
                    return end
                start = middle


if __name__ == '__main__':
    import Test

    Test.test(Solution().firstBadVersion, [
        (2, 1),
    ])
