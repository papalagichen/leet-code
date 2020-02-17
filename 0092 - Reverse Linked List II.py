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


if __name__ == '__main__':
    import Test
    import ListBuilder

    Test.test(Solution().reverseBetween, [
        ((ListBuilder.deserialize('[1,2,3,4,5]'), 2, 4), ListBuilder.deserialize('[1,4,3,2,5]')),
    ])
