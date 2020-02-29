from typing import List


# Recursive. Time: O(2^n). Space: O(2^n)
class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        for i in range(len(S)):
            if S[i].isalpha():
                results = []
                results.extend(S[:i] + S[i].upper() + x for x in self.letterCasePermutation(S[i + 1:]))
                results.extend(S[:i] + S[i].lower() + x for x in self.letterCasePermutation(S[i + 1:]))
                return results
        else:
            return [S]


# Iterative. Time: O(n). Space: O(2^n)
class Solution2:
    def letterCasePermutation(self, S: str) -> List[str]:
        results = ['']
        for c in S:
            if c.isalpha():
                a = []
                for r in results:
                    a.append(r + c.upper())
                    a.append(r + c.lower())
                results = a
            else:
                results = [r + c for r in results]
        return results


if __name__ == '__main__':
    import Test

    Test.test([Solution().letterCasePermutation, Solution2().letterCasePermutation], [
        ("a1b2", ["a1b2", "a1B2", "A1b2", "A1B2"]),
        ("3z4", ["3z4", "3Z4"]),
        ("12345", ["12345"]),
    ], sort_result=True)
