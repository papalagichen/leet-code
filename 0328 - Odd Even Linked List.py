from ListBuilder import ListNode


# Time: O(n). Space: O(1)
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head is None:
            return head
        odd, even, even_head, p = head, head.next, head.next, head.next
        if p:
            p = p.next
        if even:
            even.next = None
        counter = 3
        while p:
            if counter % 2 == 0:
                even.next, even = p, p
                p, even.next = even.next, None
            else:
                odd.next, odd = p, p
                p, odd.next = odd.next, None
            counter += 1
        odd.next = even_head
        return head


# With dummy node. Time: O(n). Space: O(1)
class Solution2:
    def oddEvenList(self, head: ListNode) -> ListNode:
        dummy_odd = odd = ListNode(0)
        dummy_even = even = ListNode(0)
        while head:
            odd.next = head
            even.next = head.next
            odd = odd.next
            even = even.next
            head = head.next.next if head.next else None
        odd.next = dummy_even.next
        return dummy_odd.next


if __name__ == '__main__':
    import Test
    import ListBuilder

    Test.test([Solution().oddEvenList, Solution2().oddEvenList], [
        (ListBuilder.deserialize('[1,2,3,4,5]'), ListBuilder.deserialize('[1,3,5,2,4]')),
        (ListBuilder.deserialize('[1,2,3]'), ListBuilder.deserialize('[1,3,2]')),
        (ListBuilder.deserialize('[1]'), ListBuilder.deserialize('[1]')),
        (ListBuilder.deserialize('[]'), ListBuilder.deserialize('[]')),
    ])
