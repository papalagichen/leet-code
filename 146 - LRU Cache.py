import collections


class LRUCache:
    def __init__(self, capacity):
        self.cache = collections.OrderedDict()
        self.capacity = capacity

    def get(self, key):
        value = self.cache.pop(key, default=-1)
        if value != -1:
            self.cache[key] = value
        return value

    def set(self, key, value):
        if self.cache and len(self.cache) >= self.capacity and key not in self.cache:
            self.cache.popitem(last=False)
        self.cache.pop(key, default=None)
        self.cache[key] = value


PREV = 0
NEXT = 1
KEY = 2
VALUE = 3


class LRUCache2:
    def __init__(self, capacity):
        self.root = root = []
        self.map = {}
        self.capacity = capacity
        root[:] = [root, root, None, None]  # doubly linked list node: [previous, next, key, value]

    def get(self, key):
        if key in self.map:
            root = self.root
            node = self.map[key]
            node[NEXT][PREV] = node[PREV]
            node[PREV][NEXT] = node[NEXT]
            node[:NEXT + 1] = root, root[1]
            node[NEXT][PREV] = node
            node[PREV][NEXT] = node
            return self.map[key][VALUE]
        return -1

    def set(self, key, value):
        if self.get(key) == -1:
            if len(self.map) == self.capacity:
                root = self.root
                last = self.root[PREV]
                root[PREV] = last[PREV]
                last[PREV][NEXT] = root
                del self.map[last[KEY]]
            node = [self.root, self.root[NEXT], key, value]
            node[NEXT][PREV] = node
            self.root[NEXT][PREV] = node
            self.root[NEXT] = node
            self.map[key] = node
        self.map[key][VALUE] = value


if __name__ == '__main__':
    import Test

    for c in (LRUCache, LRUCache2):
        cache = c(2)
        Test.equal(-1, cache.get(0))
        cache.set(5, 20)
        cache.set(6, 24)
        cache.set(7, 28)
        Test.equal(-1, cache.get(5))
        Test.equal(24, cache.get(6))
        cache.set(8, 32)
        Test.equal(24, cache.get(6))
        Test.equal(-1, cache.get(7))
        cache.set(9, 36)
        Test.equal(24, cache.get(6))
        cache.set(10, 40)
        Test.equal(24, cache.get(6))
        Test.equal(-1, cache.get(9))
        Test.equal(40, cache.get(10))

        cache = c(2)
        cache.set(2, 1)
        cache.set(1, 1)
        cache.set(2, 3)
        cache.set(4, 1)
        Test.equal(-1, cache.get(1))
        Test.equal(3, cache.get(2))

        cache = c(1)
        cache.set(2, 1)
        Test.equal(1, cache.get(2))
        cache.set(3, 2)
        Test.equal(-1, cache.get(2))
        Test.equal(2, cache.get(3))

        cache = c(2)
        cache.set(2, 1)
        cache.set(1, 1)
        cache.set(1, 2)
        cache.set(2, 2)
        Test.equal(2, cache.get(2))
        cache.set(4, 1)
        Test.equal(-1, cache.get(1))
        Test.equal(2, cache.get(2))
        Test.equal(1, cache.get(4))
