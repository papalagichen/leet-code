class Solution:
    def intToRoman(self, num):
        roman_numeral = [
            ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', ],
            ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC', ],
            ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM', ],
            ['', 'M', 'MM', 'MMM', ],
        ]

        s = ''
        while num:
            s = roman_numeral.pop(0)[num % 10] + s
            num /= 10
        return s


if __name__ == '__main__':
    import Test

    Test.test(Solution().intToRoman, [
        (1, 'I'),
        (5, 'V'),
        (10, 'X'),
        (50, 'L'),
        (100, 'C'),
        (500, 'D'),
        (1000, 'M'),
        (2, 'II'),
        (3, 'III'),
        (11, 'XI'),
        (20, 'XX'),
        (4, 'IV'),
        (9, 'IX'),
        (49, 'XLIX'),
        (97, 'XCVII'),
        (99, 'XCIX'),
        (1996, 'MCMXCVI'),
        (1904, 'MCMIV'),
    ])
