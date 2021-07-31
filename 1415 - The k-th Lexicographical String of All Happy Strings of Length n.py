import collections

"""
1, 3
a b c*

1, 4
a b c

3, 9
aba abc aca acb bab bac bca bcb cab*

2, 7
ab ac ba bc ca cb
"""


# Brute Force. Time: O(n). Space: O(1)
class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        for s in self.helper(n):
            k -= 1
            if k == 0:
                return s
        return ''

    def helper(self, n: int) -> str:
        for c in 'abc':
            if n == 1:
                yield c
            else:
                for s in self.helper(n - 1):
                    if c != s[0]:
                        yield c + s


# Brute Force. Time: O(n). Space: O(1)
class Solution2:
    def getHappyString(self, n: int, k: int) -> str:
        q = collections.deque('abc')
        while len(q[0]) < n:
            u = q.popleft()
            for v in {'a': 'bc', 'b': 'ac', 'c': 'ab'}[u[-1]]:
                q.append(u + v)
        return q[k - 1] if len(q) >= k else ''


if __name__ == '__main__':
    import Test

    Test.test([Solution().getHappyString, Solution2().getHappyString], [
        ((1, 3), 'c'),
        ((1, 4), ''),
        ((3, 9), 'cab'),
        ((2, 7), ''),
        ((2, 1), 'ab'),
        ((10, 100), 'abacbabacb'),
    ])
