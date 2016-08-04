class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        intersection_width = min(C, G) - max(A, E) if max(A, E) <= min(C, G) else 0
        intersection_height = min(D, H) - max(B, F) if max(B, F) <= min(D, H) else 0
        return (C - A) * (D - B) + (G - E) * (H - F) - intersection_width * intersection_height


class Solution2(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        intersection_width = max(min(C, G) - max(A, E), 0)
        intersection_height = max(min(D, H) - max(B, F), 0)
        return (C - A) * (D - B) + (G - E) * (H - F) - intersection_width * intersection_height


if __name__ == '__main__':
    import Test

    Test.test((Solution().computeArea, Solution2().computeArea), [
        ((-3, 0, 3, 4, 0, -1, 9, 2), 24 + 27 - 6),
        ((-2, -2, 2, 2, -2, -2, 2, 2), 16),
        ((-2, -2, 2, 2, -1, -1, 1, 1), 16),
        ((-3, -3, 3, -1, -2, -2, 2, 2), 12 + 16 - 4),
        ((-5, -2, 5, 1, -3, -3, 3, 3), 48),
        ((-2, -2, 2, 2, 3, 3, 4, 4), 17),
    ])
