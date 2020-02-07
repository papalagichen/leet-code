def isBadVersion(version):
    return version > 0


# Binary search. Time: O(lg n). Space: O(1)
class Solution:
    def firstBadVersion(self, n):
        start, end = 1, n
        while True:
            middle = (start + end) // 2
            if isBadVersion(middle):
                if middle == 1 or not isBadVersion(middle - 1):
                    return middle
                end = middle
            else:
                if end - start == 1:
                    return end
                start = middle


# Binary search. Time: O(lg n). Space: O(1)
class Solution2:
    def firstBadVersion(self, n):
        low, high = 0, n
        while low < high:
            middle = low + (high - low) // 2
            if isBadVersion(middle):
                high = middle
            else:
                low = middle + 1
        return low


if __name__ == '__main__':
    import Test

    Test.test([Solution().firstBadVersion, Solution2().firstBadVersion], [
        (2, 1),
    ])
