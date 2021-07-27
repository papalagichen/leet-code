from typing import List

"""
exactly(K) = atMost(K) - atMost(K-1)

1 2 1 2 3, 2
---------
1 2
1 2 1
  2 1
1 2 1 2
  2 1 2
    1 2 
      2 3

At most (2)
1
1 2
1 2 1
1 2 1 2
  2
  2 1
  2 1 2
    1
    1 2
      2
      2 3
        3
      
At most (1)
1
  2
    1
      2
        3
"""


# Sliding Window. Time: O(n). Space: O(n)
class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        return self.at_most_k(nums, k) - self.at_most_k(nums, k - 1)

    def at_most_k(self, nums: List[int], k: int) -> int:
        if k == 0:
            return 0
        counter = {}
        i, j, count = 0, 0, 0
        while i < len(nums):
            if j < len(nums) and (len(counter) < k or len(counter) == k and nums[j] in counter):
                counter[nums[j]] = counter.get(nums[j], 0) + 1
                j += 1
            else:
                count += j - i
                counter[nums[i]] = counter.get(nums[i], 0) - 1
                if counter[nums[i]] == 0:
                    del counter[nums[i]]
                i += 1
        return count


"""
Sliding Window with two pointers

1 2 1 2 3, 2
---------
1 2
1 2 1
  2 1
1 2 1 2
  2 1 2
    1 2 
      2 3
"""


# Two Sliding Windows. Time: O(n). Space: O(n)
class Solution2:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        counter = {}
        i, j, count, prefix = 0, 0, 0, 0
        while j < len(nums):
            counter[nums[j]] = counter.get(nums[j], 0) + 1
            if len(counter) > k:
                counter[nums[i]] -= 1
                if counter[nums[i]] == 0:
                    del counter[nums[i]]
                prefix = 0
                i += 1
            while counter[nums[i]] > 1:
                counter[nums[i]] -= 1
                if counter[nums[i]] == 0:
                    del counter[nums[i]]
                prefix += 1
                i += 1
            if len(counter) == k:
                count += prefix + 1
            j += 1
        return count


if __name__ == '__main__':
    import Test

    Test.test([Solution().subarraysWithKDistinct, Solution2().subarraysWithKDistinct], [
        ([[9], 1], 1),
        (([1, 2, 1, 2, 3], 2), 7),
        (([1, 2, 1, 3, 4], 3), 3),
        (([1, 2], 1), 2),
    ])
