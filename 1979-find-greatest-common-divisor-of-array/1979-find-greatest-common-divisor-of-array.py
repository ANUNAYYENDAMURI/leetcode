class Solution:
    def findGCD(self, nums: List[int]) -> int:
        c1=min(nums)
        c2=max(nums)
        gcd=1
        for i in range(1,min(c1,c2)+1):
            if c1%i==0 and c2%i==0:
                gcd=i
        return gcd

        