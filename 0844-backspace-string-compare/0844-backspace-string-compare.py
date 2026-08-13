class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def backspace(word):
            stack=[]
            for w in word:
                if w=="#":
                    if(stack):
                        stack.pop()
                else:
                    stack.append(w)
            return stack
        return backspace(s)==backspace(t)