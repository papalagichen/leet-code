class Solution(object):
    def deleteNode(self, node):
        prev = node
        while node.next:
            node.val = node.next.val
            prev, node = node, node.next
        prev.next = None


if __name__ == '__main__':
    import Test
    import ListBuilder

    l = ListBuilder.build(1, 2, 3, 4)
    Solution().deleteNode(l.next.next)
    Test.equal(ListBuilder.build(1, 2, 4), l)
