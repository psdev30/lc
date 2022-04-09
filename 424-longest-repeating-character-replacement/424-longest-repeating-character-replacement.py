class Solution(object):
    def characterReplacement(self, s, k):
        tracker = dict()
        longest = maxRepeatingChar = windowStart = 0
        for windowEnd in range(len(s)):
            letter = s[windowEnd]
            tracker[letter] = tracker.get(letter, 0) + 1
            maxRepeatingChar = max(maxRepeatingChar, max(tracker.values()))
            while (windowEnd - windowStart + 1) - maxRepeatingChar > k:
                leftLetter = s[windowStart]
                tracker[leftLetter] -= 1
                windowStart += 1

            longest = max(longest, windowEnd - windowStart + 1)

        return longest
        