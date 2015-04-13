from ListBuilder import ListNode, build


class Solution:
    def convertToInt(self, node):
        i = 0
        multiplier = 1
        while node is not None:
            i += multiplier * node.val
            multiplier *= 10
            node = node.next
        return i

    def convertToNode(self, i):
        head = ListNode(0)
        node = None
        while i > 0:
            if node is None:
                head = node = ListNode(i % 10)
            else:
                node.next = ListNode(i % 10)
                node = node.next
            i /= 10
        return head

    def addTwoNumbers(self, l1, l2):
        return self.convertToNode(self.convertToInt(l1) + self.convertToInt(l2))


if __name__ == '__main__':
    import Test

    Test.test(Solution().addTwoNumbers, [
        ((build(2, 4, 3), build(5, 6, 4)), build(7, 0, 8)),
    ])
