class Solution:
    def firstUniqChar(self, s: str) -> int:
        dict1={}
        b=''
        for i in s:
            if i not in dict1:
                dict1[i]=0
            dict1[i]+=1
        for i in dict1:
            if dict1[i]==1:
                b=i
                break
        for i in range(len(s)):
            if(s[i]==b):
                return i
        return -1
            

