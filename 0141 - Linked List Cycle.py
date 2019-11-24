class Solution:
    def hasCycle(self, head):
        fast, slow = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast is slow:
                return True
        return False


if __name__ == '__main__':
    import Test
    import ListBuilder

    single_node_cycle = ListBuilder.ListNode(None)
    single_node_cycle.next = single_node_cycle

    two_nodes_cycle = ListBuilder.ListNode(None)
    two_nodes_cycle.next = ListBuilder.ListNode(None)
    two_nodes_cycle.next.next = two_nodes_cycle

    cycle_list = ListBuilder.build(1, 2, 3, 4, 5)
    last = cycle_list.next.next.next.next
    last.next = cycle_list.next.next

    tail_cycle_list = ListBuilder.build(1, 2, 3)
    tail_cycle_list.next.next.next = tail_cycle_list.next.next

    Test.test(Solution().hasCycle, [
        (None, False),
        (single_node_cycle, True),
        (two_nodes_cycle, True),
        (cycle_list, True),
        (ListBuilder.build(1, 2, 3, 4, 5), False),
        (tail_cycle_list, True),
    ])
