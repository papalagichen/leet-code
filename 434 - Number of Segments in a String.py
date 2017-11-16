class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        return len(filter(lambda x: len(x) > 0, s.split(' ')))


if __name__ == '__main__':
    import Test

    Test.test(Solution().countSegments, [
        ("", 0),
        ("Hello, my name is John", 5),
        ("Hello, my name   is    John", 5),
    ])
