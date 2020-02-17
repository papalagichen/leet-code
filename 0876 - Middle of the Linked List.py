from ListBuilder import ListNode


class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        fast = slow = head
        while fast and fast.next:
            fast, slow = fast.next.next, slow.next
        return slow


if __name__ == '__main__':
    import Test
    import ListBuilder

    Test.test(Solution().middleNode, [
        (ListBuilder.deserialize('[1,2,3,4,5]'), ListBuilder.deserialize('[3,4,5]')),
        (ListBuilder.deserialize('[1,2,3,4,5,6]'), ListBuilder.deserialize('[4,5,6]')),
    ])
