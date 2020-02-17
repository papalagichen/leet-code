from ListBuilder import ListNode


# Time: O(n). Space: O(n)
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        values = []
        while head:
            values.append(head.val)
            head = head.next
        result = 0
        current = 1
        for i in reversed(values):
            if i == 1:
                result += current
            current *= 2
        return result


if __name__ == '__main__':
    import Test
    import ListBuilder

    Test.test(Solution().getDecimalValue, [
        (ListBuilder.deserialize('[1,0,1]'), 5),
        (ListBuilder.deserialize('[0]'), 0),
        (ListBuilder.deserialize('[1]'), 1),
        (ListBuilder.deserialize('[1,0,0,1,0,0,1,1,1,0,0,0,0,0,0]'), 18880),
        (ListBuilder.deserialize('[0,0]'), 0),
    ])
