import math


class Solution:
    def countPrimes(self, n):
        if n < 3:
            return 0
        primes = [True] * n
        for i in range(2, int(math.sqrt(n)) + 1):
            if primes[i]:
                j = i ** 2
                for k in range(n):
                    s = j + k * i
                    if s >= n:
                        break
                    primes[s] = False
        return primes.count(True) - 2


if __name__ == '__main__':
    import Test

    Test.test(Solution().countPrimes, [
        (0, 0),
        (1, 0),
        (2, 0),
        (3, 1),
        (4, 2),
        (5, 2),
        (10, 4),
        (100, 25),
    ])
