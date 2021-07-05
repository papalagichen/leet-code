from collections import deque

"""
00, 1, 1
*
 *

011010, 2, 3
*
   *
     *

00111010, 3, 5
*
     *

0000000000, 8, 8
*
        *
"""


# Dynamic Programming. Time: O(n). Space: O(n)
class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        s = list(s)
        s[0] = 'x'
        reaches = deque()
        for i in range(minJump, len(s)):
            if s[i - minJump] == 'x':
                reaches.append(i - minJump)
            if len(reaches) > 0 and i - reaches[0] > maxJump:
                reaches.popleft()
            if s[i] == '0' and len(reaches) > 0:
                s[i] = 'x'
        return s[-1] == 'x'


if __name__ == '__main__':
    import Test

    Test.test([Solution().canReach], [
        (('01', 1, 1), False),
        (('00', 1, 1), True),
        (('011010', 2, 3), True),
        (('01101110', 2, 3), False),
        (('00111010', 3, 5), False),
        (('0000000000', 8, 8), False)
    ])
