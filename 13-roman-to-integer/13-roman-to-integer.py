class Solution(object):
    def romanToInt(self, s):
        #even cleaner solution
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        total = roman[s[len(s) - 1]]
        for i in range(len(s) - 2, -1, -1):
            if roman[s[i]] < roman[s[i + 1]]:
                total -= roman[s[i]]
            else:
                total += roman[s[i]]
        return total
        
        
        #better solution
        #time: O(1) (same as below)
        #space: O(1)
        # roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        # total = i = 0
        # while i < len(s):
        #     if i + 1 < len(s) and roman[s[i]] < roman[s[i + 1]]:
        #         total += roman[s[i + 1]] - roman[s[i]]
        #         i += 1
        #     else:
        #         total += roman[s[i]]
        #     i += 1
        # return total
        
        
        #hashmap (the toxic af one lmao)
        #time: O(1) (max characters limited to 15 according to constraints)
        #space: O(1)
        # roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        # total = 0
        # i = 0
        # while i < len(s):
        #     if s[i] == 'I' and (i + 1 < len(s) and (s[i + 1] == 'V' or s[i + 1] == 'X')):
        #         total += roman[s[i + 1]] - roman[s[i]]
        #         i += 1
        #     elif s[i] == 'I':
        #         total += 1
        #     elif s[i] == 'X' and (i + 1 < len(s) and (s[i + 1] == 'L' or s[i + 1] == 'C')):
        #         total += roman[s[i + 1]] - roman[s[i]]
        #         i += 1
        #     elif s[i] == 'X':
        #         total += 10
        #     elif s[i] == 'C' and (i + 1 < len(s) and (s[i + 1] == 'D' or s[i + 1] == 'M')):
        #         total += roman[s[i + 1]] - roman[s[i]]
        #         i += 1
        #     elif s[i] == 'C':
        #         total += 100
        #     else:
        #         total += roman[s[i]]
        #     i += 1
        # return total