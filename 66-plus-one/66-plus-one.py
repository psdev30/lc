class Solution(object):
    def plusOne(self, digits):
        reverseDigits = digits[::-1]
        for i, val in enumerate(reverseDigits):
            if val != 9:
                reverseDigits[i] += 1
                return reverseDigits[::-1]
            elif val == 9:
                reverseDigits[i] = 0
                
        reverseDigits.append(1)
        return reverseDigits[::-1]                
            
        