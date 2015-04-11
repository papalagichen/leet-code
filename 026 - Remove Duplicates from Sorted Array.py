class Solution:
    def removeDuplicates(self, A):
        if len(A) == 0:
            return 0
        i = 0
        for j in range(1, len(A)):
            if A[i] != A[j]:
                i += 1
                A[i] = A[j]
        return i + 1

if __name__ == '__main__':
    import Test

    Test.test(Solution().removeDuplicates, [
        ([1, 1, 2], 2),
        ([1, 2], 2),
        ([1, 1, 1, 1], 1),
        ([1, 2, 2], 2),
        ([], 0),
    ], copy_parameters=False)
