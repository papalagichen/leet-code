from ListBuilder import ListNode


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev, current = None, head
        while current:
            current.next, current, prev = prev, current.next, current
        return prev


if __name__ == '__main__':
    import Test
    import ListBuilder

    Test.test(Solution().reverseList, [
        (ListBuilder.deserialize('[1,2,3,4,5]'), ListBuilder.deserialize('[5,4,3,2,1]'))
    ])
