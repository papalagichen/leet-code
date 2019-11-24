class Solution:
    # @param {ListNode} head
    # @return {void} Do not return anything, modify head in-place instead.
    def reorderList(self, head):
        # round 1. calculate length of list
        length = 0
        p = head
        while p:
            p = p.next
            length += 1

        if length <= 2:
            return

        # round 2. find the center of list, reverse the rest of list
        pp = p = head
        for i in range(-(-length / 2)):  # ceil
            pp = p
            p = p.next
        pp.next = None

        p.next, n = None, p.next
        while n:
            n.next, p, n = p, n, n.next
        tail = p

        # round 3. weave two list
        while head and tail:
            head.next, head, tail.next, tail = tail, head.next, head.next, tail.next


if __name__ == '__main__':
    import Test
    from ListBuilder import build

    Test.test(Solution().reorderList, [
        (build(1), build(1)),
        (build(1, 2), build(1, 2)),
        (build(1, 2, 3), build(1, 3, 2)),
        (build(1, 2, 3, 4), build(1, 4, 2, 3)),
    ])
