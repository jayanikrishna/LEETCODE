# Last updated: 2/23/2026, 11:25:21 PM
1class Solution:
2    def isMatch(self, s: str, p: str) -> bool:
3        # Cache to store results of (i, j) to avoid repeating work
4        memo = {}
5
6        def dfs(i, j):
7            # Check the cache first
8            if (i, j) in memo:
9                return memo[(i, j)]
10            
11            # Base Case: If we reached the end of the pattern
12            if j == len(p):
13                return i == len(s)
14
15            # Check if current characters match
16            match = i < len(s) and (s[i] == p[j] or p[j] == ".")
17
18            # Handle the '*' wildcard
19            if (j + 1) < len(p) and p[j + 1] == "*":
20                # Choice 1: Don't use the '*' (skip it and the char before it)
21                # Choice 2: Use the '*' (only if current chars match)
22                res = dfs(i, j + 2) or (match and dfs(i + 1, j))
23                memo[(i, j)] = res
24                return res
25
26            # Standard matching (no '*')
27            if match:
28                res = dfs(i + 1, j + 1)
29                memo[(i, j)] = res
30                return res
31
32            memo[(i, j)] = False
33            return False
34
35        return dfs(0, 0)