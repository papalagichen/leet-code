class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        while len(str1) > 0 and len(str2) > 0:
            if len(str1) < len(str2):
                new_str2 = str2.replace(str1, '')
                if str2 == new_str2:
                    return ''
                str2 = new_str2
            else:
                new_str1 = str1.replace(str2, '')
                if str1 == new_str1:
                    return ''
                str1 = new_str1

        return str1 if len(str2) == 0 else str2


if __name__ == '__main__':
    import Test

    Test.test(Solution().gcdOfStrings, [
        (("ABCABC", "ABC"), "ABC"),
        (("ABABAB", "ABAB"), "AB"),
        (("LEET", "CODE"), ""),
    ])
