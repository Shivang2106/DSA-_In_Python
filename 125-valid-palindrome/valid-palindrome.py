class Solution(object):
    def isPalindrome(self, s):
        c = ""
        for ch in s.lower():
            if ch.isalnum():
                c += ch
        return c == c[::-1]