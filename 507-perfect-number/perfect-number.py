class Solution(object):
    def checkPerfectNumber(self, num):
        if num <= 1:
            return False
        result = 1
        i = 2
        while i * i <= num:
            if num % i == 0:
                result += i
                if i != num // i:
                    result += num // i
            i += 1
        return result == num