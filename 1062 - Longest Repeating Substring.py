# Brute force. Time: O(n^2). Space: O(1)
class Solution:
    def longestRepeatingSubstring(self, S: str) -> int:
        longest = 0
        i = 0
        while i < len(S) - longest:
            j = i + 1
            while j < len(S) - longest:
                if S[i] == S[j]:
                    a, b = i + 1, j + 1
                    length = 1
                    while b < len(S) and S[a] == S[b]:
                        a, b, length = a + 1, b + 1, length + 1
                    longest = max(longest, length)
                    j += length
                else:
                    j += 1
            i += 1
        return longest


# Dynamic programming. Time: O(n^2). Space: O(n^2)
class Solution2:
    def longestRepeatingSubstring(self, S: str) -> int:
        longest = 0
        mem = [[0] * len(S) for _ in range(len(S))]
        for i in range(0, len(S)):
            for j in range(i + 1, len(S)):
                if S[i] == S[j]:
                    mem[i][j] = mem[i - 1][j - 1] + 1
                    longest = max(longest, mem[i][j])
        return longest


# Binary search for possible length + hash for finding duplication. Time: O(n lg n). Space: O(n^2)
class Solution3:
    def longestRepeatingSubstring(self, S: str) -> int:
        i, j = 1, len(S)
        while i <= j:
            m = i + (j - i) // 2
            if self.search_duplication(S, m):
                i = m + 1
            else:
                j = m - 1
        return i - 1

    def search_duplication(self, S: str, n: int) -> bool:
        hashes = set()
        for i in range(len(S) - n + 1):
            h = hash(S[i:i + n])
            if h in hashes:
                return True
            hashes.add(h)
        return False


if __name__ == '__main__':
    import Test

    Test.test([
        Solution().longestRepeatingSubstring,
        Solution2().longestRepeatingSubstring,
        Solution3().longestRepeatingSubstring,
    ], [
        ("abcd", 0),
        ("abbaba", 2),
        ("aabcaabdaab", 3),
        ("aaaaa", 4),
    ])
