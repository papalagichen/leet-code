class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        distance = 0
        key_positions = {x: i for i, x in enumerate(keyboard)}
        previous_key_position = 0
        for c in word:
            distance += abs(key_positions[c] - previous_key_position)
            previous_key_position = key_positions[c]
        return distance


if __name__ == '__main__':
    import Test

    Test.test(Solution().calculateTime, [
        (("abcdefghijklmnopqrstuvwxyz", "cba"), 4),
        (("pqrstuvwxyzabcdefghijklmno", "leetcode"), 73),
    ])
