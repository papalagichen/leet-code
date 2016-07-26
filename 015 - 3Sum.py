class Solution(object):
    def threeSum(self, nums):
        triplets = []

        if len(nums) < 3:
            return triplets

        nums.sort()

        for i in xrange(0, len(nums) - 2):
            target = 0 - nums[i]
            mem = {}
            for j in xrange(i + 1, len(nums)):
                n = nums[j]
                if n in mem:
                    triplet = [nums[i], mem[n], n]
                    if triplet not in triplets:
                        triplets.append(triplet)
                else:
                    mem[target - n] = n

        return triplets


if __name__ == '__main__':
    import Test

    Test.test(Solution().threeSum, [
        ([-1, 0, 1, 2, -1, -4], [
            [-1, 0, 1],
            [-1, -1, 2],
        ]),
        ([0, 0], []),
    ])
