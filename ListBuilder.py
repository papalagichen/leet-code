class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        return self.to_string()

    def __cmp__(self, other):
        return cmp(self.to_string(), other.to_string())

    def __eq__(self, other):
        return self.val == other.val

    def to_string(self):
        s = ''
        p = self
        while p:
            s += str(p.val)
            if p.next:
                s += ' -> '
            p = p.next
        return s

    def index(self, n=1):
        p = self
        while n and p:
            p = p.next
            n -= 1
        return p


def build(*a):
    if a:
        head = p = ListNode('dummy')
        for n in a:
            p.next = ListNode(n)
            p = p.next
        return head.next
    return None


if __name__ == '__main__':
    import Test

    list1 = build(1, 2, 3, 4, 5)
    list2 = build(1, 2, 3, 4, 5)
    list3 = build(2, 3, 4, 5, 6)

    Test.cmp_equal(list1, list2)
    Test.equal(ListNode(3), list1.index(2))
