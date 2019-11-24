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


if __name__ == '__main__':
    import Test

    Test.test(Solution().readBinaryWatch, [
        (0, ['0:00']),
        (1, ['8:00', '4:00', '2:00', '1:00', '0:32', '0:16', '0:08', '0:04', '0:02', '0:01']),
        (2, ['10:00', '9:00', '8:32', '8:16', '8:08', '8:04', '8:02', '8:01', '6:00', '5:00', '4:32', '4:16', '4:08',
             '4:04', '4:02', '4:01', '3:00', '2:32', '2:16', '2:08', '2:04', '2:02', '2:01', '1:32', '1:16', '1:08',
             '1:04', '1:02', '1:01', '0:48', '0:40', '0:36', '0:34', '0:33', '0:24', '0:20', '0:18', '0:17', '0:12',
             '0:10', '0:09', '0:06', '0:05', '0:03']),
    ], sort_result=True)
