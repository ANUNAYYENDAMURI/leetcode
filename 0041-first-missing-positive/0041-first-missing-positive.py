class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        a=set(nums)
        i=1
        while i in a:
            i+=1
        return i