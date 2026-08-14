class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        maxlen = 0

        for i in range(len(s)):
            dict1 = {}

            for j in range(i, len(s)):

                if s[j] not in dict1:
                    dict1[s[j]] = 0

                dict1[s[j]] += 1

                if dict1[s[j]] > 2:
                    break

                length = j - i + 1

                if length > maxlen:
                    maxlen = length

        return maxlen