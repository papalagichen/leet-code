class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        s = ''
        p = self
        while p:
            s += str(p.val)
            if p.next:
                s += ' -> '
            p = p.next
        return s

    def to_list(self):
        l = []
        p = self
        while p:
            l.append(p.val)
            p = p.next
        return l


def build(*a):
    if a:
        head = p = ListNode(a[0])
        for n in a[1:]:
            p.next = ListNode(n)
            p = p.next
        return head
    return None
