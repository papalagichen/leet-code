class Solution:
    def deleteDuplicates(self, head):
        p = head
        while p and p.next:
            if p.val == p.next.val:
                p.next = p.next.next
            else:
                p = p.next
        return head


if __name__ == '__main__':
    import Test
    from ListBuilder import build

    Test.test(Solution().deleteDuplicates, [
        (build(1), build(1)),
        (build(1, 1, 2), build(1, 2)),
        (build(1, 1, 2, 3, 3), build(1, 2, 3)),
        (build(1, 1, 1), build(1)),
    ])
