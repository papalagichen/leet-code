from typing import List

digit_to_alphabets = {
    '2': 'abc',
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrs',
    '8': 'tuv',
    '9': 'wxyz',
}


class Solution:
    # Input: "23"
    # Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
    def letterCombinations(self, digits: str) -> List[str]:
        alphabet_list = []
        for digit in digits:
            alphabet_list.append(digit_to_alphabets[digit])
        return self.permute(alphabet_list, 0, [''] * len(digits)) if digits else []

    def permute(self, alphabet_list: List[str], index: int, status: List[str]) -> List[str]:
        results = []
        for c in alphabet_list[index]:
            status[index] = c
            if index == len(alphabet_list) - 1:
                results.append(''.join(status))
            else:
                results.extend(self.permute(alphabet_list, index + 1, status))
        return results


if __name__ == '__main__':
    import Test

    Test.test(Solution().letterCombinations, [
        ('', []),
        ('23', ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]),
    ])
