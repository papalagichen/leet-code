from ListBuilder import ListNode, build


class Solution:
    def removeNthFromEnd(self, head, n):
        a = []
        p = head
        while p:
            a.append(p)
            p = p.next
        if n == len(a):
            return head.next
        a[-n - 1].next = a[-n + 1] if n > 1 else None
        return head


class Solution2:
    def removeNthFromEnd(self, head, n):
        before_remove = new_head = ListNode(0)
        before_remove.next = p = head
        while p:
            p = p.next
            n -= 1
            if n < 0:
                before_remove = before_remove.next
        before_remove.next = before_remove.next.next
        return new_head.next


if __name__ == '__main__':
    import Test

    Test.test((Solution().removeNthFromEnd, Solution2().removeNthFromEnd), [
        ((build(1, 2, 3, 4, 5), 2), build(1, 2, 3, 5)),
        ((build(1, 2, 3, 4, 5), 1), build(1, 2, 3, 4)),
        ((build(1, 2, 3, 4, 5), 5), build(2, 3, 4, 5)),
        ((build(1, 2), 1), build(1)),
        ((build(1), 1), None),
    ])
