from typing import List

"""
# 1
      1, 0
(     0, 1
()    0, 0

# 2
      2, 0
(     1, 1
((    0, 2
(()   0, 1
(())  0, 0
()    1, 0
()(   0, 1
()()  0, 0

"""


class Solution(object):
    def generateParenthesis(self, n) -> List[str]:
        return self.helper(n, 0)

    def helper(self, n, m) -> List[str]:
        res = []
        if n > 0:
            for x in self.helper(n - 1, m + 1):
                res.append('(' + x)
        if m > 0:
            for x in self.helper(n, m - 1):
                res.append(')' + x)
        if n == m == 0:
            res.append('')
        return res


if __name__ == '__main__':
    import Test

    Test.test(Solution().generateParenthesis, [
        (1, [
            "()",
        ]),
        (2, [
            "(())",
            "()()",
        ]),
        (3, [
            "((()))",
            "(()())",
            "(())()",
            "()(())",
            "()()()",
        ]),
    ], sort_result=True)
