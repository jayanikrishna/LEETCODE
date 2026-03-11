# Last updated: 3/11/2026, 11:45:47 PM
1class Solution:
2    def longestValidParentheses(self, s: str) -> int:
3        max_len = 0
4        # Initialize stack with -1 to handle the base case
5        stack = [-1]
6        
7        for i, char in enumerate(s):
8            if char == '(':
9                # Push the index of '('
10                stack.append(i)
11            else:
12                # We found a ')', so pop the last '(' or boundary
13                stack.pop()
14                
15                if not stack:
16                    # If stack is empty, this ')' is a new boundary
17                    stack.append(i)
18                else:
19                    # Valid substring found: current index minus 
20                    # the index of the last unmatched element
21                    max_len = max(max_len, i - stack[-1])
22                    
23        return max_len