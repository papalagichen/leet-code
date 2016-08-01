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


# https://discuss.leetcode.com/topic/25382/sharing-explanation-of-the-solution
class Solution2(object):
    def singleNumber(self, nums):
        xor, a, b = 0, 0, 0
        for num in nums:
            xor ^= num
        mask = 1
        while xor & mask == 0:
            mask <<= 1
        for num in nums:
            if num & mask:
                a ^= num
            else:
                b ^= num
        return [a, b]


if __name__ == '__main__':
    import Test

    Test.test((Solution().singleNumber, Solution2().singleNumber), [
        ([1, 2, 1, 3, 2, 5], [3, 5]),
        ([0, 1, 1, 2], [0, 2]),
    ])
