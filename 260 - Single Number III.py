class Solution(object):
    def singleNumber(self, nums):
        result = []
        nums.sort()
        i = 0
        while i < len(nums) - 2:
            if nums[i] != nums[i + 1]:
                result.append(nums[i])
                if nums[i + 1] != nums[i + 2]:
                    result.append(nums[i + 1])
                if len(result) == 2:
                    return result
                i += 1
            else:
                i += 2
        return result + nums[len(result) - 2:]


if __name__ == '__main__':
    import Test

    Test.test(Solution().singleNumber, [
        ([1, 2, 1, 3, 2, 5], [3, 5]),
        ([0, 1, 1, 2], [0, 2]),
    ])
