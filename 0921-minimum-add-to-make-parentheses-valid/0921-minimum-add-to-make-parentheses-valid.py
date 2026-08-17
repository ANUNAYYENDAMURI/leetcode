class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        c=0
        stack=[]
        for i in s:
            if i == '(':
                stack.append(i)
            elif i==')' and len(stack)>=1:
                stack.pop()
            else:
                c+=1
        return len(stack)+c


