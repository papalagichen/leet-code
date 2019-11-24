from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit, low, high = 0, 0, 0
        for i in range(len(prices)):
            if prices[i] > prices[high]:
                high = i
            elif prices[i] < prices[high]:
                max_profit += prices[high] - prices[low]
                high = low = i
            elif prices[i] < prices[low]:
                high = low = i
        return max_profit + prices[high] - prices[low] if prices else 0


if __name__ == '__main__':
    import Test

    Test.test(Solution().maxProfit, [
        ([], 0),
        ([7, 1, 5, 3, 6, 4], 7),
        ([1, 2, 3, 4, 5], 4),
        ([7, 6, 4, 3, 1], 0),
        ([2, 4, 1], 2),
    ])
