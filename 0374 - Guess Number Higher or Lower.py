def guess(num):
    if num > 6:
        return -1
    elif num < 6:
        return 1
    else:
        return 0


class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        low, high = 0, n
        while low < high:
            mid = (low + high) / 2
            if guess(mid) == 1:
                low = mid + 1
            else:
                high = mid
        return low


class Solution2(object):
    def guessNumber(self, n):
        lo, hi = 1, n
        while lo < hi:
            mid = (lo + hi) / 2
            lo, hi = ((mid, mid), (mid + 1, hi), (lo, mid - 1))[guess(mid)]
        return lo


if __name__ == '__main__':
    import Test

    Test.test([Solution().guessNumber, Solution2().guessNumber], [
        (10, 6),
        (100000, 6),
    ])
