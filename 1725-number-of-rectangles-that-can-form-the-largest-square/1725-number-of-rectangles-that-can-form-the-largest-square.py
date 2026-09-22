class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        a=[]
        dict1={}
        for r in range(len(rectangles)):
            a.append(min(rectangles[r]))
        for i in a:
            if i not in dict1:
                dict1[i]=0
            dict1[i]+=1
        return dict1[max(dict1)]