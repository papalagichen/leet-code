import re

ord_base = ord('a') - 1


class Solution:
    def freqAlphabets(self, s: str) -> str:
        result = []
        i = len(s) - 1
        while i >= 0:
            if s[i] == '#':
                result.insert(0, self.get_char(int(s[i - 2:i])))
                i -= 3
            else:
                result.insert(0, self.get_char(int(s[i])))
                i -= 1
        return ''.join(result)

    def get_char(self, n: int) -> str:
        return chr(ord_base + n)


class Solution2:
    def freqAlphabets(self, s: str) -> str:
        return ''.join(chr(ord_base + int(i[:2])) for i in re.findall(r'\d\d#|\d', s))


if __name__ == '__main__':
    import Test

    Test.test([Solution().freqAlphabets, Solution2().freqAlphabets], [
        ("10#11#12", "jkab"),
        ("1326#", "acz"),
        ("25#", "y"),
        ("12345678910#11#12#13#14#15#16#17#18#19#20#21#22#23#24#25#26#", "abcdefghijklmnopqrstuvwxyz"),
    ])
