class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        all_upper = True
        all_lower = True
        capitalized = True
        for i in range(len(word)):
            if word[i].isupper():
                all_lower = False
            if word[i].islower():
                all_upper = False
            if word[i].isupper() and i > 0:
                capitalized = False
        return all_upper or all_lower or capitalized


if __name__ == '__main__':
    import Test

    Test.test(Solution().detectCapitalUse, [
        ("USA", True),
        ("Google", True),
        ("GooglE", False),
        ("google", True),
        ("A", True),
        ("a", True),
        ("FFf", False),
    ])
