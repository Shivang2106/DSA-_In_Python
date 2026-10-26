class Solution(object):
    def reverseWords(self, s):
        a = s.split()
        c = a[::-1]
        return " ".join(c)