class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        letterTracker = dict()
        longestSubstr = windowStart = 0
        for windowEnd in range(len(s)):
            letter = s[windowEnd]
            letterTracker[letter] = letterTracker.get(letter, 0) + 1
            if len(letterTracker) > k:
                leftLetter = s[windowStart]
                letterTracker[leftLetter] -= 1
                if letterTracker[leftLetter] == 0:
                    del letterTracker[leftLetter]
                windowStart += 1

            longestSubstr = max(longestSubstr, windowEnd - windowStart + 1)

        return longestSubstr
        