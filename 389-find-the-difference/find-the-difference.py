class Solution(object):
    def findTheDifference(self, s, t):
        a=sorted(s)
        b=sorted(t)
        a.append(" ")
        for i in range(len(b)):
            if a[i] != b[i]:
                return b[i]
        return b[-1]