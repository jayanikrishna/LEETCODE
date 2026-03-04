# Last updated: 3/4/2026, 8:13:27 PM
1class Solution:
2    def isValid(self, s: str) -> bool:
3        # Map each closing bracket to its opening counterpart
4        close_to_open = {")": "(", "]": "[", "}": "{"}
5        stack = []
6
7        for char in s:
8            # If the character is a closing bracket
9            if char in close_to_open:
10                # If stack is not empty and top matches the opener
11                if stack and stack[-1] == close_to_open[char]:
12                    stack.pop()
13                else:
14                    return False
15            else:
16                # It's an opening bracket, push to stack
17                stack.append(char)
18        
19        # Return True only if all brackets were closed
20        return True if not stack else False