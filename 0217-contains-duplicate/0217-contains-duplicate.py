class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dict1={}
        c=0
        for i in range(len(nums)):
            if nums[i] not in dict1:
                dict1[nums[i]]=0
            dict1[nums[i]]+=1
        for i in dict1.values():
            if i>=2:
                c+=1
                break
        return c==1