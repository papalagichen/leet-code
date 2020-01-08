from typing import List


class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        i, j = 0, len(A) - 1
        while i != j:
            if A[i] % 2 == 0:
                i += 1
            elif A[j] % 2 == 1:
                j -= 1
            else:
                A[i], A[j] = A[j], A[i]
        return A


if __name__ == '__main__':
    import Test

    Test.test(Solution().sortArrayByParity, [
        ([3, 1, 2, 4], [4, 2, 1, 3]),
    ])
