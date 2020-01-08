from typing import List


class Solution:
    def shortestDistance(self, words: List[str], word1: str, word2: str) -> int:
        p1 = p2 = 0
        shortest_distance = len(words)
        while p1 < len(words) and p2 < len(words):
            if words[p1] == word1 and words[p2] == word2:
                shortest_distance = min(shortest_distance, abs(p1 - p2))
                if p1 < p2:
                    p1 += 1
                else:
                    p2 += 1
                continue
            if words[p1] != word1:
                p1 += 1
            if words[p2] != word2:
                p2 += 1
        return shortest_distance

    def shortestDistance2(self, words: List[str], word1: str, word2: str) -> int:
        p1 = p2 = shortest_distance = len(words)
        for i in range(len(words)):
            if words[i] == word1:
                p1 = i
                shortest_distance = min(shortest_distance, abs(p1 - p2))
            if words[i] == word2:
                p2 = i
                shortest_distance = min(shortest_distance, abs(p1 - p2))
        return shortest_distance


if __name__ == '__main__':
    import Test

    Test.test([Solution().shortestDistance, Solution().shortestDistance2], [
        ((["practice", "makes", "perfect", "coding", "makes"], "coding", "practice"), 3),
        ((["practice", "makes", "perfect", "coding", "makes"], "makes", "coding"), 1),
        ((["practice", "makes"], "makes", "practice"), 1),
        ((["a", "c", "b", "b", "a"], "a", "b"), 1),
    ])
