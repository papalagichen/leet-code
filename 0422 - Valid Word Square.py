from typing import List


class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        c = 0
        for i in range(max(len(words), len(words[c]))):
            for j in range(i, max(len(words), len(words[c]))):
                w1 = words[i][j] if j < len(words[i]) else ''
                w2 = words[j][i] if j < len(words) and i < len(words[j]) else ''
                if w1 != w2:
                    return False
            c += 1
        return True


class Solution2:
    def validWordSquare(self, words: List[str]) -> bool:
        for i in range(len(words)):
            if words[i] != ''.join(line[i] for line in words if i < len(line)):
                return False
        return True


if __name__ == '__main__':
    import Test

    Test.test([Solution().validWordSquare, Solution2().validWordSquare], [
        (
            [
                "abcd",
                "bnrt",
                "crmy",
                "dtye"
            ],
            True
        ),
        (
            [
                "abcd",
                "bnrt",
                "crm",
                "dt"
            ],
            True
        ),
        (
            [
                "ball",
                "area",
                "read",
                "lady"
            ],
            False
        ),
        (
            [
                "ball",
                "asee",
                "let",
                "lep"
            ],
            False
        ),
        (
            [
                "abc",
                "b"
            ],
            False
        ),
        (
            [
                "abc",
                "bde",
                "cefg"
            ],
            False
        )
    ])
