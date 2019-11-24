class Solution(object):
    def isPalindrome(self, head):
        if head is None or head.next is None:
            return True
        if head.next.next is None:
            return head.val == head.next.val
        # find the middle
        slow, fast = head, head.next
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        if fast.next:
            fast = fast.next
            slow.next, slow = None, slow.next.next
        else:
            slow.next, slow = None, slow.next
        # reverse second half part
        p, p.next, slow, n = slow, None, slow.next, slow.next.next if slow.next else None
        while slow:
            p, slow.next, slow, n = slow, p, n, n.next if n else None
        while head and fast:
            if head.val != fast.val:
                return False
            head, fast = head.next, fast.next
        return head is None and fast is None


if __name__ == '__main__':
    import Test
    import ListBuilder

    Test.test(Solution().isPalindrome, [
        (None, True),
        (ListBuilder.build(1), True),
        (ListBuilder.build(1, 1), True),
        (ListBuilder.build(1, 0, 0), False),
        (ListBuilder.build(1, 2, 3, 4, 3, 2, 1), True),
        (ListBuilder.build(1, 2, 3, 4, 4, 3, 2, 1), True),
        (ListBuilder.build(1, 2, 3, 4, 3, 2, 5), False),
    ])
