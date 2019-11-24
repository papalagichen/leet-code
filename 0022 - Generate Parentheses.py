class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        


if __name__ == '__main__':
    import Test

    Test.test(Solution().generateParenthesis, [
        (3, ["((()))",
             "(()())",
             "(())()",
             "()(())",
             "()()()"]),
    ])
