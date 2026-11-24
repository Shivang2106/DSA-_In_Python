class Solution(object):
    def maxLength(self, nums):

        def prod(arr):
            pro = 1
            for i in arr:
                pro *= i
            return pro

        def gcd(a, b):
            while b:
                temp = a
                a = b
                b = temp % b
            return a

        def gcd_arr(arr):
            result = arr[0]
            for i in arr[1:]:
                result = gcd(result, i)
            return result

        def lcm(a, b):
            return (a // gcd(a, b)) * b

        def lcm_arr(arr):
            result = arr[0]
            for i in arr[1:]:
                result = lcm(result, i)
            return result

        count = 0

        for i in range(len(nums)):
            arr = []

            for j in range(i, len(nums)):
                arr.append(nums[j])

                if prod(arr) == gcd_arr(arr) * lcm_arr(arr):
                    count = max(count, len(arr))

        return count
