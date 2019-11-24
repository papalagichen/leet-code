class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        return len(list(filter(lambda x: x, s.split(' '))))


class Solution2(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """

        is_space = True
        count = 0

        for i in s:
            if i == ' ':
                if not is_space:
                    is_space = True
            else:
                if is_space:
                    is_space = False
                    count += 1
        return count


if __name__ == '__main__':
    import Test

    Test.test(Solution().countSegments, [
        ("", 0),
        ("Hello, my name is John", 5),
        ("Hello, my name   is    John", 5),
    ])

    Test.test(Solution2().countSegments, [
        ("", 0),
        ("Hello, my name is John", 5),
        ("Hello, my name   is    John", 5),
    ])
