class Solution(object):
    def thirdMax(self, nums):
        len_nums = len(nums)
        max_numbers = nums[0:1]
        for n in nums[1:]:
            m = min(3, len(max_numbers), len_nums)
            for i in range(m):
                if n == max_numbers[i]:
                    break
                elif n > max_numbers[i]:
                    max_numbers.insert(i, n)
                    break
                elif i == m - 1 and len(max_numbers) < 3:
                    max_numbers.append(n)
        return max_numbers[2] if len(max_numbers) > 2 else max_numbers[0]


if __name__ == '__main__':
    import Test

    Test.test(Solution().thirdMax, [
        ([3, 2, 1], 1),
        ([1, 2], 2),
        ([2, 2, 3, 1], 1),
        ([2, 2, 2, 2], 2),
        ([2, 2, 2, 1], 2),
        ([5, 2, 2], 5),
        ([1, 2, 2], 2),
    ])
