from ListBuilder import ListNode


# Copy to extra list and then two pointers. Time: O(n). Space: O(n)
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        values = []
        while head:
            values.append(head.val)
            head = head.next
        start, end = 0, len(values) - 1
        while start < end:
            if values[start] != values[end]:
                return False
            start += 1
            end -= 1
        return True


# Reverse second half in-place. Time: O(n). Space: O(1)
class Solution2:
    def isPalindrome(self, head: ListNode) -> bool:
        if head is None:
            return True
        # find the middle
        fast = slow = head
        while fast and fast.next:
            fast, slow = fast.next.next, slow.next
        # reverse the second half
        temp, slow = slow, slow.next
        if fast is None:
            temp.next = None
        while slow:
            temp, slow.next, slow = slow, temp, slow.next
        # check palindrome
        while head and temp and head is not temp:
            if head.val != temp.val:
                return False
            head, temp = head.next, temp.next
        return True


if __name__ == '__main__':
    import Test
    import ListBuilder

    Test.test([Solution().isPalindrome, Solution2().isPalindrome], [
        (None, True),
        (ListBuilder.build(1), True),
        (ListBuilder.build(1, 1), True),
        (ListBuilder.build(1, 0, 0), False),
        (ListBuilder.build(1, 2, 3, 4, 3, 2, 1), True),
        (ListBuilder.build(1, 2, 3, 4, 4, 3, 2, 1), True),
        (ListBuilder.build(1, 2, 3, 4, 3, 2, 5), False),
    ])
