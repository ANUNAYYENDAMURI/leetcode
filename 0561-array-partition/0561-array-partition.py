class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        a=sorted(nums)
        sum1=0
        for i in range(len(nums)):
            if i%2==0:
                sum1+=a[i]
        return sum1