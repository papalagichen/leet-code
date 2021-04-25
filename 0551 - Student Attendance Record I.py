class Solution:
    def checkRecord(self, s: str) -> bool:
        absent = 0
        late = 0
        is_late = False
        for c in s:
            if c == 'L':
                late += 1
                if late >= 3:
                    is_late = True
            else:
                late = 0
            if c == 'A':
                absent += 1
        return not is_late and absent < 2


if __name__ == '__main__':
    import Test

    Test.test(Solution().checkRecord, [
        ("PPALLP", True),
        ("PPALLL", False),
    ])
