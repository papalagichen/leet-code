import bisect


class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = 0

    def add(self, key: int) -> None:
        self.data |= 1 << key

    def remove(self, key: int) -> None:
        self.data &= ~(1 << key)

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        return self.data & (1 << key) > 0


class MyHashSet2:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = []

    def add(self, key: int) -> None:
        index = bisect.bisect_left(self.data, key)
        if index == len(self.data) or self.data[index] != key:
            self.data.insert(index, key)

    def remove(self, key: int) -> None:
        index = bisect.bisect_left(self.data, key)
        if index < len(self.data) and self.data[index] == key:
            self.data = self.data[:index] + self.data[index + 1:]

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        index = bisect.bisect_left(self.data, key)
        return index < len(self.data) and self.data[index] == key


if __name__ == '__main__':
    hashSet = MyHashSet()
    hashSet.add(1)
    hashSet.add(2)
    assert hashSet.contains(1)
    assert not hashSet.contains(3)
    hashSet.add(2)
    assert hashSet.contains(2)
    hashSet.remove(2)
    hashSet.contains(2)

    hashSet = MyHashSet2()
    hashSet.add(1)
    hashSet.add(2)
    assert hashSet.contains(1)
    assert not hashSet.contains(3)
    hashSet.add(2)
    assert hashSet.contains(2)
    hashSet.remove(2)
    hashSet.contains(2)
