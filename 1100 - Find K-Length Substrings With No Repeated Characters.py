# Brute force. Time: O(n * K). Space: O(K)
class Solution:
    def numKLenSubstrNoRepeats(self, S: str, K: int) -> int:
        num = 0
        word_dict = dict()
        word_list = list()
        for i in range(len(S)):
            if len(word_list) == K - 1 and all(count <= 1 for _, count in word_dict.items()) and S[i] not in word_dict:
                num += 1
            word_dict[S[i]] = word_dict.get(S[i], 0) + 1
            word_list.append(S[i])
            if len(word_list) == K:
                c = word_list.pop(0)
                if word_dict[c] == 1:
                    del word_dict[c]
                else:
                    word_dict[c] = word_dict.get(c) - 1
        return num


# Sliding window. Time: O(n). Space: O(K)
class Solution2:
    def numKLenSubstrNoRepeats(self, S: str, K: int) -> int:
        num = 0
        last_repeat_index = -1
        word_dict = {}
        for i in range(len(S)):
            last_repeat_index = max(last_repeat_index, word_dict.get(S[i], -1))
            if i - last_repeat_index >= K:
                num += 1
            word_dict[S[i]] = i
        return num


# Sliding window. Time: O(n * k). Space: O(K)
class Solution3:
    def numKLenSubstrNoRepeats(self, S, K):
        res, i = 0, 0
        cur = set()
        for j in range(len(S)):
            while S[j] in cur:
                cur.remove(S[i])
                i += 1
            cur.add(S[j])
            res += j - i + 1 >= K
        return res


if __name__ == '__main__':
    import Test

    Test.test([Solution().numKLenSubstrNoRepeats, Solution3().numKLenSubstrNoRepeats], [
        (('havefunonleetcode', 5), 6),
        (('home', 5), 0),
        (('abcddefgh', 5), 1),
    ])
