class Solution(object):
    def isHappy(self, n):
        seen = set()

        while n not in seen:
            seen.add(n)

            output = 0
            while n != 0:
                digit = (n % 10) ** 2
                output += digit
                n = n // 10

            n = output
            if n == 1: 
                return True

        return False
        