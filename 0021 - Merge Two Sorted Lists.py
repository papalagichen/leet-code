from ListBuilder import ListNode


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
    from ListBuilder import build
    import Test

    Test.test(Solution().mergeTwoLists, [
        ((build(1, 3, 5), build(2, 4, 6, 8)), build(1, 2, 3, 4, 5, 6, 8)),
        ((build(1, 3, 5), None), build(1, 3, 5)),
        ((None, None), None)
    ])
