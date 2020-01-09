class Solution:
    def twoSum(self, nums, target):
        mem = {}
        for i, n in enumerate(nums):
            if n in mem:
                return mem[n], i
            rest = target - n
            mem[rest] = i


class Solution2:
    def twoSum(self, nums, target):
        mem = {}
        for i, n in enumerate(nums):
            if target - n in mem:
                return mem[target - n], i
            mem[n] = i


if __name__ == '__main__':
    import Test

    Test.test([Solution().twoSum, Solution2().twoSum], [
        (((2, 7, 11, 15), 9), (0, 1)),
    ])
