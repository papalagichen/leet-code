class Solution:
    def removeElement(self, A, elem):
        i = 0
        for j in range(len(A)):
            if A[j] != elem:
                A[i] = A[j]
                i += 1
        return i


if __name__ == '__main__':
    import Test

    Test.test(Solution().removeElement, [
        (([1, 2, 2, 3, 4], 2), 3),
        (([1, 2, 2, 3, 4], 5), 5),
        (([], 0), 0),
        (([1], 1), 0),
    ], copy_parameters=False)
