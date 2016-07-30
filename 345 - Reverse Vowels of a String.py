class Solution(object):
    def reverseVowels(self, s):
        vowels = []
        result = []
        for c in s:
            if c.lower() in 'aeiou':
                vowels.append(c)
        i = len(vowels) - 1
        for c in s:
            if c.lower() in 'aeiou':
                result.append(vowels[i])
                i -= 1
            else:
                result.append(c)
        return ''.join(result)


class Solution2(object):
    def reverseVowels(self, s):
        cs = list(s)
        i, j = 0, len(cs) - 1
        while i < j:
            while i < j and cs[i].lower() not in 'aeiou':
                i += 1
            while i < j and cs[j].lower() not in 'aeiou':
                j -= 1
            cs[i], cs[j] = cs[j], cs[i]
            i, j = i + 1, j - 1
        return ''.join(cs)


if __name__ == '__main__':
    import Test

    Test.test((Solution().reverseVowels, Solution2().reverseVowels), [
        ('', ''),
        ('bcdfg', 'bcdfg'),
        ('hello', 'holle'),
        ('leetcode', 'leotcede'),
        ('aA', 'Aa'),
    ])
