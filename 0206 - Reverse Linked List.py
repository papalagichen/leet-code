class Solution:
    def reverseList(self, head):
        p, c = None, head
        while c:
            n, c.next = c.next, p
            p, c = c, n
        return p


if __name__ == '__main__':
    import Test
    from ListBuilder import build

    Test.test(Solution().reverseList, [
        (None, None),
        (build(1, 2, 3, 4, 5), build(5, 4, 3, 2, 1))
    ])
