class Solution:
    def majorityElement(self, nums):
        half_length = len(nums) / 2
        d = {}
        for i in nums:
            if i in d:
                d[i] += 1
                if d[i] > half_length:
                    return i
            else:
                d[i] = 1
        return nums[0]


class Solution2:
    def majorityElement(self, nums):
        return sorted(nums)[(len(nums) // 2)]


if __name__ == '__main__':
    import Test

    Test.test((Solution().majorityElement, Solution2().majorityElement), [
        ([2], 2),
        ([1, 1, 1, 2, 3], 1),
    ])
