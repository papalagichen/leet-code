class Solution:
    def reverseWords(self, s: str) -> str:
        start = 0
        results = []
        for i, c in enumerate(s):
            if c == ' ':
                results.append(''.join(reversed(s[start:i])))
                start = i + 1
        return ' '.join(results + [''.join(reversed(s[start:]))])


class Solution2:
    def reverseWords(self, s: str) -> str:
        start = 0
        results = ''
        for i, c in enumerate(s):
            if c == ' ':
                results += (s[i - 1:start - 1:-1] if start > 0 else s[i - 1::-1]) + ' '
                start = i + 1
        return results + (s[:start - 1:-1] if start > 0 else s[::-1])


class Solution3:
    def reverseWords(self, s: str) -> str:
        return ' '.join(x[::-1] for x in s.split(' '))


class Solution4:
    def reverseWords(self, s: str) -> str:
        return ' '.join(s.split()[::-1])[::-1]


if __name__ == '__main__':
    import Test

    Test.test([Solution().reverseWords, Solution2().reverseWords, Solution3().reverseWords, Solution4().reverseWords], [
        ("Let's take LeetCode contest", "s'teL ekat edoCteeL tsetnoc"),
    ])
