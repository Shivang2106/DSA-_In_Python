class Solution(object):
    def capitalizeTitle(self, title):
        string = title.split()
        result = []

        for word in string:
            if len(word) <= 2:
                result.append(word.lower())
            else:
                result.append(word.capitalize())

        return " ".join(result)