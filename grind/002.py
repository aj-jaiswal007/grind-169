class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if not stack or char in {"{", "(", "["}:
                stack.append(char)
            else:
                top = stack[-1]
                if char == "}" and top == "{" or char == ")" and top == "(" or char == "]" and top == "[":
                    stack.pop() 
                else:
                    stack.append(char)
    
        return not stack
        

        
        
if __name__ == "__main__":
    s = Solution()
    print(s.isValid("(])"))