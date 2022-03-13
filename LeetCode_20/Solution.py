from fileinput import close


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {")": "(", "]": "[", "}": "{"}

        for c in s:
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        return True if not stack else False
                    
        

def main():
    s = Solution()
    print(s.isValid("()[]{}"))
    print(s.isValid("([)]"))

if __name__ == '__main__':
    main()