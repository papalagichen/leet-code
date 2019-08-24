class Solution:
    # Input: "abccccdd"
    # Output: 7
    # Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.
    def longestPalindrome(self, s: str) -> int:
        d = {}
        for c in s:
            d[c] = d.get(c, 0) + 1
        count = 0
        single = 0
        for v in d.values():
            count += v
            if v % 2 == 1:
                single = 1
                count -= 1
        return count + single


if __name__ == '__main__':
    import Test

    Test.test(Solution().longestPalindrome, [
        ('abccccdd', 7),
        ('ccc', 3),
        ('cc', 2),
        ('c', 1),
    ])
