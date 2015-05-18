class Solution:
    def detectCycle(self, head):
        fast, slow = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast is slow:
                fast = head
                while fast is not slow:
                    fast = fast.next
                    slow = slow.next
                return fast
        return None


if __name__ == '__main__':
    import Test
    import ListBuilder

    single_node_cycle = ListBuilder.ListNode(1)
    single_node_cycle.next = single_node_cycle

    two_nodes_cycle = ListBuilder.ListNode(1)
    two_nodes_cycle.next = ListBuilder.ListNode(2)
    two_nodes_cycle.next.next = two_nodes_cycle

    cycle_list = ListBuilder.build(1, 2, 3, 4, 5)
    last = cycle_list.next.next.next.next
    last.next = cycle_list.next.next

    tail_cycle_list = ListBuilder.build(1, 2, 3)
    tail_cycle_list.next.next.next = tail_cycle_list.next.next

    func = Solution().detectCycle
    Test.equal(None, func(None))
    Test.equal(1, func(single_node_cycle).val)
    Test.equal(1, func(two_nodes_cycle).val)
    Test.equal(3, func(cycle_list).val)
    Test.equal(None, func(ListBuilder.build(1, 2, 3, 4, 5)))
    Test.equal(3, func(tail_cycle_list).val)
