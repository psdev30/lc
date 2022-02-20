class Solution(object):
    def romanToInt(self, s):
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        total = 0
        i = 0
        while i < len(s):
            if s[i] == 'I' and (i + 1 < len(s) and (s[i + 1] == 'V' or s[i + 1] == 'X')):
                sumToAdd = roman[s[i + 1]] - roman[s[i]]
                total += sumToAdd
                i += 1
            elif s[i] == 'I':
                total += 1
            elif s[i] == 'X' and (i + 1 < len(s) and (s[i + 1] == 'L' or s[i + 1] == 'C')):
                sumToAdd = roman[s[i + 1]] - roman[s[i]]
                total += sumToAdd
                i += 1
            elif s[i] == 'X':
                total += 10
            elif s[i] == 'C' and (i + 1 < len(s) and (s[i + 1] == 'D' or s[i + 1] == 'M')):
                sumToAdd = roman[s[i + 1]] - roman[s[i]]
                total += sumToAdd
                i += 1
            elif s[i] == 'C':
                total += 100
            else:
                total += roman[s[i]]
            i += 1
        return total