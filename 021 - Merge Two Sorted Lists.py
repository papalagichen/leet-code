from ListBuilder import ListNode, build


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
    node = Solution().mergeTwoLists(build((1, 3, 5)), build((2, 4, 6, 8)))
    while node:
        print(node.val)
        node = node.next

    print

    node = Solution().mergeTwoLists(build((1, 3, 5)), None)
    while node:
        print(node.val)
        node = node.next

    print

    print Solution().mergeTwoLists(None, None)
