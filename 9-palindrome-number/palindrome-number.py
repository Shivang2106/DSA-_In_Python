class Solution(object):
    def isPalindrome(self, x):
        s = 0
        num = x
        while num > 0:
            r = num % 10
            s = (s * 10) + r
            num = num // 10
        if x == s:
            return True
        else:
            return False