from typing import List

"""
["a", "banana", "app", "appl", "ap", "apply", "apple"]

{'a': {'p': {'p': {'l': {'e': {}, 'y': {}}}}}}
"""


# Trie. Time: O(n). Space: O(n)
class Solution:
    def longestWord(self, words: List[str]) -> str:
        trie = dict()
        longest = ''
        for w in sorted(words):
            p = trie
            for i in range(len(w) - 1):
                if w[i] not in p:
                    break
                p = p[w[i]]
            else:
                p[w[-1]] = dict()
                if len(w) > len(longest):
                    longest = w
        return longest


if __name__ == '__main__':
    import Test

    Test.test([Solution().longestWord], [
        (['a'], 'a'),
        (["w", "wo", "wor", "worl", "world"], "world"),
        (["a", "banana", "app", "appl", "ap", "apply", "apple"], "apple"),
        (["yo", "ew", "fc", "zrc", "yodn", "fcm", "qm", "qmo", "fcmz", "z", "ewq", "yod", "ewqz", "y"], "yodn"),
        (["m", "mo", "moc", "moch", "mocha", "l", "la", "lat", "latt", "latte", "c", "ca", "cat"], "latte"),
        (["rac", "rs", "ra", "on", "r", "otif", "o", "onpdu", "rsf", "rs", "ot", "oti", "racy", "onpd"], "otif"),
    ])
