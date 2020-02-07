class Solution:
    def removeVowels(self, S: str) -> str:
        return ''.join(x for x in S if x not in set('aeiou'))


if __name__ == '__main__':
    import Test

    Test.test(Solution().removeVowels, [
        ("leetcodeisacommunityforcoders", "ltcdscmmntyfrcdrs"),
        ("aeiou", ""),
    ])
