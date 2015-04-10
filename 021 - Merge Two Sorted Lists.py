class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1, l2):
        head = p = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                p.next = l1
                l1 = l1.next
            else:
                p.next = l2
                l2 = l2.next
            p = p.next
        p.next = l1 if l1 else l2
        return head.next


if __name__ == '__main__':
    l1 = ListNode(1)
    l1.next = ListNode(3)
    l1.next.next = ListNode(5)
    l2 = ListNode(2)
    l2.next = ListNode(4)
    l2.next.next = ListNode(6)
    l2.next.next.next = ListNode(8)
    node = Solution().mergeTwoLists(l1, l2)
    while node:
        print(node.val)
        node = node.next

    print

    l1 = ListNode(1)
    l1.next = ListNode(3)
    l1.next.next = ListNode(5)
    node = Solution().mergeTwoLists(l1, None)
    while node:
        print(node.val)
        node = node.next

    print

    print Solution().mergeTwoLists(None, None)
