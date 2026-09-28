class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        dict1={}
        for i in nums:
            if i not in dict1:
                dict1[i]=0
            dict1[i]+=1
        s=0
        for k in dict1:
            if dict1[k]==1:
                s+=k
        return s


        