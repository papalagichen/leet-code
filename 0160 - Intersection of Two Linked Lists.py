class Solution:
    def getIntersectionNode(self, a, b):
        if a is None or b is None:
            return None
        if a is b:
            return a
        sum_a, tail_a = self.sum_and_tail_of_list(a)
        sum_b, tail_b = self.sum_and_tail_of_list(b)
        if tail_a is not tail_b:
            return None
        self.reverse_list(a)
        sum_c, _ = self.sum_and_tail_of_list(b)
        sum_a_without_intersection = ((sum_a - sum_b) + sum_c) / 2
        self.reverse_list(tail_a)
        last = None
        while sum_a_without_intersection > 0:
            sum_a_without_intersection -= a.val
            last = a
            a = a.next
        return last

    def reverse_list(self, node):
        a, b = None, node
        while b:
            c, b.next = b.next, a
            a, b = b, c

    def sum_and_tail_of_list(self, node):
        s, tail = 0, None
        while node:
            s += node.val
            tail, node = node, node.next
        return s, tail


class Solution2:
    def getIntersectionNode(self, a, b):
        if a is None or b is None:
            return None
        len_a, len_b, counter = 0, 0, 0
        head_a, head_b = a, b
        while a is not b:
            a = a.next
            b = b.next
            counter += 1
            if (a is None or b is None) and counter == len_a + len_b:
                return None
            if a is None:
                len_a = counter
                a = head_b
            if b is None:
                len_b = counter
                b = head_a
        return a

if __name__ == '__main__':
    import Test
    from ListBuilder import build

    list1 = build(1, 2, 3, 4, 5, 6)
    a, b = Solution().sum_and_tail_of_list(list1)
    list2 = build(3)
    list3 = build(1)
    list2.next = list1.index(3)
    list4 = list1.index(3)
    list5 = list6 = build(1)
    Test.test((Solution().getIntersectionNode, Solution2().getIntersectionNode), [
        ((None, None), None),
        ((list1, list2), list1.index(3)),
        ((list2, list3), None),
        ((list1, list4), list1.index(3)),
        ((list5, list6), list5),
    ])
