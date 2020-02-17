from ListBuilder import ListNode


# Time: O(n). Space: O(1)
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        start, prev = None, None
        p = head
        original_m = m
        while p:
            m -= 1
            n -= 1
            if m == 0:
                start = p
            if m <= 0:
                p.next, p, prev = prev, p.next, p
                if n == 0:
                    if start.next:
                        start.next.next = prev
                    start.next = p
                    break
            else:
                prev, p = p, p.next
        return prev if original_m == 1 else head


# With dummy node + fast forward. Time: O(n). Space: O(1)
class Solution2:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        prev = dummy = ListNode(0)
        dummy.next = head
        for _ in range(m - 1):
            prev, head = head, head.next
        for _ in range(n - m):
            temp = head.next
            head.next = temp.next
            temp.next = prev.next
            prev.next = temp
        return dummy.next


if __name__ == '__main__':
    import Test
    import ListBuilder

    Test.test([Solution().reverseBetween, Solution2().reverseBetween], [
        ((ListBuilder.deserialize('[1,2,3,4,5]'), 2, 4), ListBuilder.deserialize('[1,4,3,2,5]')),
        ((ListBuilder.deserialize('[1,2]'), 1, 2), ListBuilder.deserialize('[2,1]')),
        ((ListBuilder.deserialize('[1]'), 1, 1), ListBuilder.deserialize('[1]')),
        ((ListBuilder.deserialize('[]'), 0, 0), ListBuilder.deserialize('[]')),
    ])
