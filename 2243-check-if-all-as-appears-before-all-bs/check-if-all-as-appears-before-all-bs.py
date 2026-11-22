class Solution(object):
    def checkString(self, s):
        count = 0
        for i in range(len(s)):
            if s[i] == "a" and count == 0:
                continue
            elif s[i] == "b":
                count = 1
            if s[i] =="a" and count ==1:
                return False
        return True