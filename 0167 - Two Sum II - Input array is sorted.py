import bisect
from typing import List


# Time O(n lg n), space O(1)
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            index = bisect.bisect_left(numbers, target - numbers[i])
            if i != index and numbers[index] == target - numbers[i]:
                return [i + 1, index + 1]


# Time O(n), space O(1)
class Solution2:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, j = 0, len(numbers) - 1
        while numbers[i] + numbers[j] != target:
            if numbers[i] + numbers[j] < target:
                i += 1
            else:
                j -= 1
        return [i + 1, j + 1]


if __name__ == '__main__':
    import Test

    Test.test([Solution().twoSum, Solution2().twoSum], [
        (([2, 7, 11, 15], 9), [1, 2]),
        (([0, 2, 3, 4, 5, 7, 9], 8), [3, 5]),
        (([-1, 0], -1), [1, 2]),
    ])
