class Solution:
    def findTheDistanceValue(self, arr1,arr2,d):
        ans=0
        for i in range(len(arr1)):
            v=True
            for j in range(len(arr2)):

                a=abs(arr1[i]-arr2[j])
                if a<=d:
                    v=False
                    break
            if v:
                ans+=1
        return ans 

        