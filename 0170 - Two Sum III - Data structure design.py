import bisect


class TwoSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.mem = []

    def add(self, number: int) -> None:
        """
        Add the number to an internal data structure..
        """
        index = bisect.bisect_left(self.mem, number)
        self.mem.insert(index, number)

    def find(self, value: int) -> bool:
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        """
        if len(self.mem) == 0:
            return False
        i, j = 0, len(self.mem) - 1
        while i != j:
            s = self.mem[i] + self.mem[j]
            if s < value:
                i += 1
            elif s > value:
                j -= 1
            else:
                return True
        return False


class TwoSum2:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.mem = {}

    def add(self, number: int) -> None:
        """
        Add the number to an internal data structure..
        """
        self.mem[number] = self.mem.get(number, 0) + 1

    def find(self, value: int) -> bool:
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        """
        for n in self.mem:
            diff = value - n
            if diff in self.mem:
                if diff == n and self.mem.get(diff) == 1:
                    continue
                return True
        return False


if __name__ == '__main__':
    import Test

    two_sum = TwoSum()
    two_sum.add(1)
    two_sum.add(3)
    two_sum.add(5)
    two_sum.add(5)

    two_sum2 = TwoSum2()
    two_sum2.add(1)
    two_sum2.add(3)
    two_sum2.add(5)
    two_sum2.add(5)

    Test.test([two_sum.find, two_sum2.find], [
        (4, True),
        (7, False),
        (2, False),
        (10, True),
    ])

    two_sum = TwoSum()
    two_sum.add(0)
    two_sum.add(-1)
    two_sum.add(1)

    two_sum2 = TwoSum2()
    two_sum2.add(0)
    two_sum2.add(-1)
    two_sum2.add(1)

    Test.test([two_sum.find, two_sum2.find], [
        (0, True),
    ])
