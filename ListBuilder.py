class ListNode:
    def __init__(self, x):
            self.val = x
            self.next = None


def build(*a):
    if a:
        head = p = ListNode(a[0])
        for n in a[1:]:
            p.next = ListNode(n)
            p = p.next
        return head
    return None
