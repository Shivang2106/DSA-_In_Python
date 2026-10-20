class Solution(object):
    def fizzBuzz(self, n):
        list1 = []
        for i in range(1,n+1):
            if i%3==0 and i%5==0:
                a="FizzBuzz"
                list1.append(a)
            elif i%3==0:
                a="Fizz"
                list1.append(a)
            elif i%5 ==0:
                a="Buzz"
                list1.append(a)
            else:
                a=str(i)
                list1.append(a)
        return list1