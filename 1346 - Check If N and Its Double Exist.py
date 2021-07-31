from typing import List


class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        nums = set()
        zero_count = 0
        for n in arr:
            if n == 0:
                zero_count += 1
                if zero_count > 1:
                    return True
            nums.add(n)
        for n in arr:
            if n != 0 and n * 2 in nums:
                return True
        return False


class Solution2:
    def checkIfExist(self, arr: List[int]) -> bool:
        if arr.count(0) > 1:
            return True
        nums = set(arr)
        for n in arr:
            if n != 0 and n * 2 in nums:
                return True
        return False


if __name__ == '__main__':
    import Test

    Test.test([Solution().checkIfExist, Solution2().checkIfExist], [
        ([10, 2, 5, 3], True),
        ([7, 1, 14, 11], True),
        ([3, 1, 7, 11], False),
        ([-2, 0, 10, -19, 4, 6, -8], False),
    ])
