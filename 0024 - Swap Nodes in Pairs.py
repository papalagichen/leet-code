from ListBuilder import ListNode


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        prev, current, head = None, head, head.next
        while current and current.next:
            a, b, current = current, current.next, current.next.next
            if prev:
                prev.next = b
            a.next, b.next, prev = current, a, a
        return head


if __name__ == '__main__':
    import Test
    import ListBuilder

    Test.test(Solution().swapPairs, [
        (ListBuilder.build(1, 2, 3, 4), ListBuilder.build(2, 1, 4, 3)),
        (ListBuilder.build(1, 2, 3), ListBuilder.build(2, 1, 3)),
        (ListBuilder.build(1), ListBuilder.build(1)),
    ])
