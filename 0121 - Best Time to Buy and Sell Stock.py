from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit, lowest, highest = 0, 0, 0
        for i in range(len(prices)):
            if prices[i] < prices[lowest]:
                highest = lowest = i
            elif prices[i] > prices[highest]:
                highest = i
            max_profit = max(prices[highest] - prices[lowest], max_profit)
        return max_profit

    def maxProfit2(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0
        max_profit, lowest, highest = 0, prices[0], prices[0]
        for p in prices:
            if p < lowest:
                highest = lowest = p
            elif p > highest:
                highest = p
            max_profit = max(highest - lowest, max_profit)
        return max_profit


if __name__ == '__main__':
    import Test

    Test.test((Solution().maxProfit, Solution().maxProfit2), [
        ([], 0),
        ([7, 1, 5, 3, 6, 4], 5),
        ([7, 6, 4, 3, 1], 0),
        ([2, 4, 1], 2),
    ])
