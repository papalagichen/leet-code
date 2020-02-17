from ListBuilder import ListNode


# Time: O(n). Space: O(1)
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        prev, p, start, start_prev = None, head, None, None
        while p:
            if p.next and p.val == p.next.val and start is None:
                start, start_prev = p, prev
            elif (p.next is None or p.val != p.next.val) and start:
                if start_prev:
                    start_prev.next = p.next
                if start is head:
                    head = p.next
                prev, p, start = start_prev, p.next, None
                continue
            prev, p = p, p.next
        return head


# With dummy node + fast forward. Time: O(n). Space: O(1)
class Solution2:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        prev = dummy = ListNode(None)
        dummy.next = head
        while head and head.next:
            if head.val == head.next.val:
                while head.next and head.val == head.next.val:
                    head = head.next
                prev.next = head = head.next
            else:
                prev, head = head, head.next
        return dummy.next


if __name__ == '__main__':
    import Test
    import ListBuilder

    Test.test([Solution().deleteDuplicates, Solution2().deleteDuplicates], [
        (ListBuilder.deserialize('[1,2,3,3,4,4,5]'), ListBuilder.deserialize('[1,2,5]')),
        (ListBuilder.deserialize('[1,1,1,2,3]'), ListBuilder.deserialize('[2,3]')),
    ])
