class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        length = len(s)
        for c in range(1, (length / 2) + 1):
            if length % c == 0:
                pattern = s[:c]
                for i in range(c, length, c):
                    if pattern != s[i:i + c]:
                        break
                    if i + c == length:
                        return True
        return False


if __name__ == '__main__':
    import Test

    Test.test(Solution().repeatedSubstringPattern, [
        ('abab', True),
        ('aba', False),
        ('abcabcabcabc', True),
        ('aaa', True),
    ])
