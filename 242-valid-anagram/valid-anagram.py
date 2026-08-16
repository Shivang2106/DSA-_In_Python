class Solution(object):
    def isAnagram(self, s, t):
        a = s.lower()
        b = t.lower()
        if len(a) != len(b):
            return False
        for ch in a:
            if a.count(ch) != b.count(ch):
                return False
        return True