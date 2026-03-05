# Last updated: 3/6/2026, 12:03:38 AM
1class Solution:
2    def generateParenthesis(self, n: int) -> list[str]:
3        res = []
4        stack = []
5
6        def backtrack(open_count, close_count):
7            # Base Case: We've used all n pairs
8            if open_count == close_count == n:
9                res.append("".join(stack))
10                return
11            
12            # Choice 1: Add an opening parenthesis
13            if open_count < n:
14                stack.append("(")
15                backtrack(open_count + 1, close_count)
16                stack.pop() # Backtrack: remove it before the next choice
17            
18            # Choice 2: Add a closing parenthesis
19            if close_count < open_count:
20                stack.append(")")
21                backtrack(open_count, close_count + 1)
22                stack.pop() # Backtrack: remove it before the next choice
23
24        backtrack(0, 0)
25        return res