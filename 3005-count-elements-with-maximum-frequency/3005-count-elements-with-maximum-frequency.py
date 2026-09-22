class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        dict1={}
        for i in nums:
            if i not in dict1:
                dict1[i]=0
            dict1[i]+=1
        m=max(dict1.values())
        ans=0
        for i in dict1:
            if dict1[i]==m:
                ans+=dict1[i]
        return ans