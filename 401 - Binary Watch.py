from typing import List


class Solution:
    # Input: 1
    # Return: ["1:00", "2:00", "4:00", "8:00", "0:01", "0:02", "0:04", "0:08", "0:16", "0:32"]
    # hours: 0-11
    # minutes: 0-59
    def readBinaryWatch(self, num: int) -> List[str]:
        if num == 0:
            return ['0:00']
        return self.permute_time([0] * 10, 0, num)

    def permute_time(self, nums: List[int], start: int, count: int) -> List[str]:
        results = []
        count -= 1
        for i in range(start, len(nums) - count):
            nums[i] = 1
            if count > 0:
                results.extend(self.permute_time(nums, i + 1, count))
            elif count == 0:
                hours, minutes = self.get_time_string(nums)
                if 0 <= hours < 12 and 0 <= minutes < 60:
                    results.append(f"{hours}:{minutes:02}")
            nums[i] = 0
        return results

    def get_time_string(self, nums: List[int]) -> (int, int):
        hour = 0
        for i in range(4):
            hour <<= 1
            hour += nums[i]

        minute = 0
        for i in range(4, len(nums)):
            minute <<= 1
            minute += nums[i]

        return hour, minute


print(Solution().readBinaryWatch(0))
print(Solution().readBinaryWatch(1))
print(Solution().readBinaryWatch(2))
