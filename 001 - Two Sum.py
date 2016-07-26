class Solution:
    def twoSum(self, num, target):
        mem = {}
        for i, n in enumerate(num):
            if n in mem:
                return mem[n], i
            rest = target - n
            mem[rest] = i

if __name__ == '__main__':
    import Test

    Test.test(Solution().twoSum, [
        (((2, 7, 11, 15), 9), (0, 1)),
    ])
