"""
aeiaaioaaaaeiiiiouuuooaauuaeiu
      --------------
                   13

aeeeiiiioooauuuaeiou
               -----
               12345

starting with a
ending with u
"""


# Dynamic Programming. Time: O(n). Space: O(1)
class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        longest = 0
        length = 1
        charset = set(word[0])
        for i in range(1, len(word)):
            if word[i] < word[i - 1]:
                length = 1
                charset.clear()
                charset.add(word[i])
            else:
                length += 1
                charset.add(word[i])
                if len(charset) == 5:
                    longest = max(longest, length)
        return longest


if __name__ == '__main__':
    import Test

    Test.test([Solution().longestBeautifulSubstring], [
        ('aeiaaioaaaaeiiiiouuuooaauuaeiu', 13),
        ('aeeeiiiioooauuuaeiou', 5),
        ('a', 0),
    ])
