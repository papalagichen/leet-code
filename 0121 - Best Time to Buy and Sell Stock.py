from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit, lowest, highest = 0, 0, 0
        for i in range(len(prices)):
            if prices[i] < prices[lowest]:
                highest = lowest = i
            elif prices[i] > prices[highest]:
                highest = i
            profit = prices[highest] - prices[lowest]
            if profit > max_profit:
                max_profit = profit
        return max_profit


if __name__ == '__main__':
    import Test

    Test.test(Solution().maxProfit, [
        ([], 0),
        ([7, 1, 5, 3, 6, 4], 5),
        ([7, 6, 4, 3, 1], 0),
        ([2, 4, 1], 2),
    ])
