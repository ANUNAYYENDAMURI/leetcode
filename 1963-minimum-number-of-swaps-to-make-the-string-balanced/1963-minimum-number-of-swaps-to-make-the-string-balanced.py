class Solution:
    def minSwaps(self, s: str) -> int:
        open = 0
        swaps = 0

        for ch in s:
            if ch == '[':
                open += 1
            else:
                open -= 1

            if open < 0:
                swaps += 1
                open = 1

        return swaps