class Solution(object):
    def reverseDegree(self, s):
        sum = 0

        for i in range(len(s)):
            sum = sum + (ord("z")-ord(s[i])+1)*(i+1)
        return sum