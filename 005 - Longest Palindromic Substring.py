class Solution:
    def longestPalindrome(self, s):
        if len(s) < 2:
            return s
        counters = [[0, 0, True]]  # [start, length, finished]
        for i in range(1, len(s)):
            for c in filter(lambda x: not x[2], counters):
                if c[0] > 0 and s[c[0] - 1] == s[i]:
                    c[0] -= 1
                    c[1] += 2
                else:
                    c[2] = True
            if i > 1 and s[i - 2] == s[i]:
                counters.append([i - 2, 3, False])
            if s[i - 1] == s[i]:
                counters.append([i - 1, 2, False])
        longest = max(counters, key=lambda x: x[1])
        return s[longest[0]:longest[0] + longest[1]]


class Solution2:
    def longestPalindrome(self, s):
        for length in xrange(len(s), 0, -1):
            for start in xrange(0, len(s) - length + 1):
                ss = s[start:start + length]
                if ss == ss[::-1]:
                    return s[start:start + length]


if __name__ == '__main__':
    import Test

    Test.test((Solution().longestPalindrome, Solution2().longestPalindrome), [
        ('81992797182647891712321872618337', '12321'),
        ('12321', '12321'),
        ('123321', '123321'),
        ('1233215', '123321'),
        ('5123321', '123321'),
        ('1', '1'),
        ('11', '11'),
        ('111', '111'),
        ('1111', '1111'),
        ('iopsajhffgvrnyitusobwcxgwlwniqchfnssqttdrnqqcsrigjsxkzcmuoiyxzerakhmexuyeuhjfobrmkoqdljrlojjjysfdslyvckxhuleagmxnzvikfitmkfhevfesnwltekstsueefbrddxrmxokpaxsenwlgytdaexgfwtneurhxvjvpsliepgvspdchmhggybwupiqaqlhjjrildjuewkdxbcpsbjtsevkppvgilrlspejqvzpfeorjmrbdppovvpzxcytscycgwsbnmspihzldjdgilnrlmhaswqaqbecmaocesnpqaotamwofyyfsbmxidowusogmylhlhxftnrmhtnnljjhhcfvywsqimqxqobfsageysonuoagmmviozeouutsiecitrmkypwknorjjiaasxfhsftypspwhvqovmwkjuehujofiabznpipidhfxpoustquzyfurkcgmioxacleqdxgrxbldcuxzgbcazgfismcgmgtjuwchymkzoiqhzaqrtiykdkydgvuaqkllbsactntexcybbjaxlfhyvbxieelstduqzfkoceqzgncvexklahxjnvtyqcjtbfanzgpdmucjlqpiolklmjxnscjcyiybdkgitxnuvtmoypcdldrvalxcxalpwumfx', 'ykdky'),
        ('e' * 1000, 'e' * 1000),
    ])
