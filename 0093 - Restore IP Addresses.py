from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        return list(set(self.helper(s, 4, [])))

    def helper(self, s: str, segment_count: int, path: List[str]) -> List[str]:
        if segment_count == 0 and s != '' or segment_count > 0 and s == '':
            return []
        elif segment_count == 0 and s == '' and len(path) == 4:
            return ['.'.join(path)]
        valid_addresses = []
        for i in range(1, min(3, len(s)) + 1):
            if (s[0] != '0' or len(s[:i]) == 1) and int(s[:i]) <= 255:
                valid_addresses += self.helper(s[i:], segment_count - 1, path + [s[:i]])
        return valid_addresses


if __name__ == '__main__':
    import Test

    Test.test(Solution().restoreIpAddresses, [
        ("25525511135", ["255.255.11.135", "255.255.111.35"]),
        ("0000", ["0.0.0.0"]),
        ("00000", []),
        ("010010", ["0.10.0.10", "0.100.1.0"]),
    ], sort_result=True)
