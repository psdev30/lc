class Solution(object):
    def characterReplacement(self, s, k):
        tracker = dict()
        longest = windowStart = 0
        for windowEnd in range(len(s)):
            letter = s[windowEnd]
            tracker[letter] = tracker.get(letter, 0) + 1
            while (windowEnd - windowStart + 1) - max(tracker.values()) > k:
                leftLetter = s[windowStart]
                tracker[leftLetter] -= 1
                windowStart += 1

            longest = max(longest, windowEnd - windowStart + 1)

        return longest
        