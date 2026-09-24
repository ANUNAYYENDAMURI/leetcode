class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        m=101
        for i in range(len(nums)):
            j=nums[i]
            s=0
            while j>0:
                dig=j%10
                j//=10
                s+=dig
            if s==i:
                m=min(m,i)
        if m==101:
            return -1
        return m            
