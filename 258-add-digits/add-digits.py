class Solution(object):
    def addDigits(self, num):
        s=0
        while num>0:
            r=num%10
            s=s+r
            num=num//10   
        if s>9:
            return self.addDigits(s)
        return s