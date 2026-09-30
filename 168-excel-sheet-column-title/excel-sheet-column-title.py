class Solution(object):
    def convertToTitle(self, columnNumber):
        result = ""
        list1=['A','B','C','D',
        'E','F','G','H','I','J',
        'K','L','M','N','O','P',
        'Q','R','S','T','U','V',
        'W','X','Y','Z']
        while columnNumber :
            columnNumber -=1
            r = columnNumber%26
            columnNumber =columnNumber//26
            result = list1[r] +result
        return result 