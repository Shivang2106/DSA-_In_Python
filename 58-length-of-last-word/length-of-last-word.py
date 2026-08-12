class Solution(object):
    def lengthOfLastWord(self, s):
        a = s.strip()[::-1]

        for i in range(len(a)):
            if a[i] == " ":
                return i

        return len(a)
