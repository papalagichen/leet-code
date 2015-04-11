class Solution:
    def countAndSay(self, n):
        say = '1'
        for i in range(n - 1):
            s = last = ''
            count = 0
            for c in say + ' ':
                if c != last:
                    if count > 0:
                        s += str(count) + last
                    count = 1
                    last = c
                else:
                    count += 1
            say = s
        return say


class Solution2:
    def countAndSay(self, n):
        say = '1'
        for i in range(n - 1):
            s = ''
            while say:
                c, say = say[0], say[1:]
                count = 1
                while say and c == say[0]:
                    say = say[1:]
                    count += 1
                s += str(count) + c
            say = s
        return say


class Solution3:
    def countAndSay(self, n):
        say = '1'
        for i in range(n - 1):
            j = 0
            s = ''
            while j < len(say):
                count = 1
                while j + 1 < len(say) and say[j] == say[j + 1]:
                    count += 1
                    j += 1
                s += str(count) + say[j]
                j += 1
            say = s
        return say


if __name__ == '__main__':
    import Test

    Test.test(Solution().countAndSay, [
        (1, '1'),
        (2, '11'),
        (3, '21'),
        (4, '1211'),
        (5, '111221'),
        (6, '312211'),
    ])
    Test.test(Solution2().countAndSay, [
        (1, '1'),
        (2, '11'),
        (3, '21'),
        (4, '1211'),
        (5, '111221'),
        (6, '312211'),
    ])
    Test.test(Solution3().countAndSay, [
        (1, '1'),
        (2, '11'),
        (3, '21'),
        (4, '1211'),
        (5, '111221'),
        (6, '312211'),
    ])