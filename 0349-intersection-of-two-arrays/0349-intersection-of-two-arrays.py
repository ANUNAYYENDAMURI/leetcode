class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        a=set(nums1)
        b=set(nums2)
        x=[]
        y=[]
        for i in a:
            if i not in b:
                x.append(i)
        for i in b:
            if i not in a:
                y.append(i)
        return list(set(a) & set(b))