# Last updated: 3/5/2026, 11:59:19 PM
1class Solution:
2    def longestPalindrome(self, s: str) -> str:
3        if not s or len(s) < 1:
4            return ""
5        
6        start, end = 0, 0
7        
8        def expandAroundCenter(left: int, right: int) -> int:
9            while left >= 0 and right < len(s) and s[left] == s[right]:
10                left -= 1
11                right += 1
12            # Return the length of the palindrome found
13            return right - left - 1
14
15        for i in range(len(s)):
16            # Case 1: Odd length (center is s[i])
17            len1 = expandAroundCenter(i, i)
18            # Case 2: Even length (center is between s[i] and s[i+1])
19            len2 = expandAroundCenter(i, i + 1)
20            
21            max_len = max(len1, len2)
22            
23            # If we found a longer palindrome, update our start/end pointers
24            if max_len > (end - start):
25                start = i - (max_len - 1) // 2
26                end = i + max_len // 2
27                
28        return s[start:end + 1]