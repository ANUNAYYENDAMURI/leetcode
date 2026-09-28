class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        n=len(nums)
        a=set(nums)
        a=sorted(a,reverse=True)
        if len(a)<3:
            return a[0]
        return a[2]