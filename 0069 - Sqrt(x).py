class Solution:
    def mySqrt(self, x: int) -> int:
        low, high = 0, x / 2
        while low < high:
            middle = int((low + high) / 2)
            product = middle * middle
            if product == x or product < x < (middle + 1) ** 2:
                return middle
            elif product > x:
                high = middle - 1
            else:
                low = middle + 1
        return low


if __name__ == '__main__':
    import Test

    Test.test(Solution().mySqrt, [
        (4, 2),
        (8, 2),
        (0, 0),
    ])
