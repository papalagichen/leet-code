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
    print([1, 2, 3, 5] == Solution().removeNthFromEnd(build(1, 2, 3, 4, 5), 2).to_list())
    print([1, 2, 3, 4] == Solution().removeNthFromEnd(build(1, 2, 3, 4, 5), 1).to_list())
    print([2, 3, 4, 5] == Solution().removeNthFromEnd(build(1, 2, 3, 4, 5), 5).to_list())
    print([1] == Solution().removeNthFromEnd(build(1, 2), 1).to_list())
    print(None == Solution().removeNthFromEnd(build(1), 1))

    print([1, 2, 3, 5] == Solution2().removeNthFromEnd(build(1, 2, 3, 4, 5), 2).to_list())
    print([1, 2, 3, 4] == Solution2().removeNthFromEnd(build(1, 2, 3, 4, 5), 1).to_list())
    print([2, 3, 4, 5] == Solution2().removeNthFromEnd(build(1, 2, 3, 4, 5), 5).to_list())
    print([1] == Solution2().removeNthFromEnd(build(1, 2), 1).to_list())
    print(None == Solution2().removeNthFromEnd(build(1), 1))