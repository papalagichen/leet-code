import bisect


class MyHashMap:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.keys = []
        self.values = []

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        index = bisect.bisect_left(self.keys, key)
        if index < len(self.keys) and self.keys[index] == key:
            self.keys[index] = key
            self.values[index] = value
        else:
            self.keys.insert(index, key)
            self.values.insert(index, value)

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        index = bisect.bisect_left(self.keys, key)
        if 0 <= index < len(self.keys) and self.keys[index] == key:
            return self.values[index]
        return -1

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        index = bisect.bisect_left(self.keys, key)
        if 0 <= index < len(self.keys) and self.keys[index] == key:
            self.keys = self.keys[:index] + self.keys[index + 1:]
            self.values = self.values[:index] + self.values[index + 1:]


if __name__ == '__main__':
    hashMap = MyHashMap()
    hashMap.put(1, 1)
    hashMap.put(2, 2)
    assert hashMap.get(1) == 1
    assert hashMap.get(3) == -1
    hashMap.put(2, 1)
    assert hashMap.get(2) == 1
    hashMap.remove(2)
    assert hashMap.get(2) == -1
