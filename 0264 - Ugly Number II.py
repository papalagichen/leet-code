import heapq

"""
   [1]
1  [2 3 5]
2  [3 4 5 6 10]
3  [4 5 6 9 10 15]
4  [5 6 8 9 10 12 15 20]
"""


# Time: O(n log n). Space: O(n)
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        nums = []
        heapq.heappush(nums, 1)
        for i in range(1, n):
            first = heapq.heappop(nums)
            while len(nums) > 0 and first == nums[0]:
                heapq.heappop(nums)
            for x in (2, 3, 5):
                heapq.heappush(nums, first * x)
        return nums[0]


# Time: O(n). Space: O(n)
class Solution2:
    def nthUglyNumber(self, n: int) -> int:
        i2, i3, i5 = 0, 0, 0
        nums = [1]
        while len(nums) != n:
            m = min(2 * nums[i2], 3 * nums[i3], 5 * nums[i5])
            if m != nums[-1]:
                nums.append(m)
            if nums[-1] == 2 * nums[i2]:
                i2 += 1
            elif nums[-1] == 3 * nums[i3]:
                i3 += 1
            elif nums[-1] == 5 * nums[i5]:
                i5 += 1
        return nums[n - 1]


if __name__ == '__main__':
    import Test

    Test.test([Solution().nthUglyNumber, Solution2().nthUglyNumber], [
        (10, 12),
        (1, 1),
    ])
