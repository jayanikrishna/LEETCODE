# Last updated: 3/7/2026, 11:52:24 PM
1class Solution:
2    def strStr(self, haystack: str, needle: str) -> int:
3        n, h = len(needle), len(haystack)
4        
5        # If the needle is longer than the haystack, it can't be found
6        if n > h:
7            return -1
8            
9        # The loop range ensures we don't look past the end of the haystack
10        # We stop at h - n + 1
11        for i in range(h - n + 1):
12            # Extract a substring of length n and compare
13            if haystack[i:i + n] == needle:
14                return i
15                
16        return -1