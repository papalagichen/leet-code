from typing import List

from ListBuilder import ListNode


class Solution:
    def splitListToParts(self, root: ListNode, k: int) -> List[ListNode]:
        p = root
        length = 0
        while p is not None:
            length += 1
            p = p.next
        result = []
        head, tail = root, root
        while len(result) < k and tail is not None:
            i = 1
            head = tail
            while i < (length // k) + (0 if len(result) >= length % k else 1):
                tail = tail.next
                i += 1
            tail, temp = tail.next, tail
            temp.next = None
            result.append(head)
        while len(result) < k:
            result.append(None)
        return result


if __name__ == '__main__':
    import Test
    import ListBuilder

    Test.test(Solution().splitListToParts, [
        (
            (ListBuilder.deserialize('[1, 2, 3]'), 5),
            ListBuilder.deserialize('[[1],[2],[3],[],[]]')
        ),
        (
            (ListBuilder.deserialize('[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]'), 3),
            ListBuilder.deserialize('[[1, 2, 3, 4], [5, 6, 7], [8, 9, 10]]')
        ),
    ])
