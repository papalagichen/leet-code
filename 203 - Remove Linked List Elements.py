from ListBuilder import ListNode


class Solution:
    def removeElements(self, head, val):
        p = node = ListNode(None)
        node.next = head
        while p and p.next:
            if p.next.val == val:
                p.next = p.next.next
            else:
                p = p.next
        return node.next


if __name__ == '__main__':
    import Test
    from ListBuilder import build

    Test.test(Solution().removeElements, [
        ((build(1, 2, 6, 3, 4, 5, 6), 6), build(1, 2, 3, 4, 5)),
        ((build(1, 2, 6, 3, 4, 5, 6), 1), build(2, 6, 3, 4, 5, 6)),
        ((build(1, 1), 1), None)
    ])
