class Solution:
    def isPalindrome(self, s):
        left, right = 0, len(s) - 1
        while left < right:
            if not s[left].isalnum():
                left += 1
            elif not s[right].isalnum():
                right -= 1
            elif s[left].lower() == s[right].lower():
                left += 1
                right -= 1
            else:
                return False
        return True


if __name__ == '__main__':
    import Test

    Test.test(Solution().isPalindrome, [
        ("", True),
        ("A", True),
        ("A man, a plan, a canal: Panama", True),
        ("race a car", False),
        ("1a2", False),
    ])
