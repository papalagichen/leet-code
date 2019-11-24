class Solution(object):
    def wordPattern(self, pattern, str):
        tokens = str.split(' ')
        if len(tokens) != len(pattern):
            return False
        d = {}
        for i in range(len(pattern)):
            if pattern[i] in d and d[pattern[i]] != tokens[i] or tokens[i] in d.values() and pattern[i] not in d:
                return False
            d[pattern[i]] = tokens[i]
        return True


if __name__ == '__main__':
    import Test

    Test.test(Solution().wordPattern, [
        (('abba', 'dog cat cat dog'), True),
        (('abba', 'dog cat cat fish'), False),
        (('aaaa', 'dog cat cat dog'), False),
        (('abba', 'dog dog dog dog'), False),
        (('jquery', 'jquery'), False)
    ])
