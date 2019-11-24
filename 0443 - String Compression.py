from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        count = 1
        current_char = chars[0]
        current_index = 0
        for i in range(1, len(chars)):
            if current_char != chars[i]:
                next_char = chars[i]
                chars[current_index] = current_char
                if count > 1:
                    c = list(str(count))
                    chars[current_index + 1:current_index + 1 + len(c)] = c
                    current_index += len(c)
                current_index += 1
                current_char = next_char
                count = 1
            else:
                count += 1
        chars[current_index] = current_char
        if count > 1:
            c = list(str(count))
            chars[current_index + 1:current_index + 1 + len(c)] = c
            current_index += len(c)
        current_index += 1
        return current_index


a = ['a']
print(Solution().compress(a))
print(a)
