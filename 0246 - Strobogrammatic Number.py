class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        i, j = 0, len(num) - 1
        while i < j:
            if num[i] == '1' and num[j] == '1' or \
            num[i] == '6' and num[j] == '9' or \
            num[i] == '8' and num[j] == '8' or \
            num[i] == '9' and num[j] == '6' or \
            num[i] == '0' and num[j] == '0':
                i, j = i + 1, j - 1
            else:
                return False
        if i == j and num[i] not in ('0', '1', '8'):
            return False
        return True


if __name__ == '__main__':
    import Test

    Test.test(Solution().isStrobogrammatic, [
        ("0", True),
        ("1", True),
        ("2", False),
        ("6", False),
        ("8", True),
        ("11", True),
        ("66", False),
        ("69", True),
        ("88", True),
        ("00", True),
        ("962", False),
    ])
