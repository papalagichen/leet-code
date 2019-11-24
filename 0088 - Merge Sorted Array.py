class Solution:
    def merge(self, A, m, B, n):
        i, j = m - 1, n - 1
        for p in range(m + n - 1, -1, -1):
            if (i >= 0 and j >= 0 and A[i] < B[j]) or (i < 0 <= j):
                A[p] = B[j]
                j -= 1
            else:
                A[p] = A[i]
                i -= 1


if __name__ == '__main__':
    A = [1, 3, 5, 7]
    B = [2, 4, 6, 8, 10]
    A.extend([0] * len(B))
    Solution().merge(A, len(A) - len(B), B, len(B))
    if A == [1, 2, 3, 4, 5, 6, 7, 8, 10]:
        print('OK!')
    else:
        print(A)
    A = []
    B = [1]
    A.extend([0] * len(B))
    Solution().merge(A, len(A) - len(B), B, len(B))
    if A == [1]:
        print('OK!')
    else:
        print(A)
