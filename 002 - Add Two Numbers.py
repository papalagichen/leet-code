# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


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
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)
    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)
    node = Solution().addTwoNumbers(l1, l2)
    while node is not None:
        print node.val,
        if node.next is not None:
            print ' -> ',
        node = node.next
