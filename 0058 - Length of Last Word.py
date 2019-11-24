class Solution:
    def lengthOfLastWord(self, s):
        s = s.strip()
        try:
            return len(s) - 1 - s.rindex(' ')
        except ValueError:
            return len(s)


class Solution2:
    def lengthOfLastWord(self, s):
        count = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] != ' ':
                count += 1
            elif count > 0:
                break
        return count


if __name__ == '__main__':
    import Test

    Test.test((Solution().lengthOfLastWord, Solution2().lengthOfLastWord), [
        ('Hello World', 5),
        ('Hello', 5),
        ('', 0),
        (' a ', 1),
    ])
