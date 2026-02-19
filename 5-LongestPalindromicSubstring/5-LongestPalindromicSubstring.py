# Last updated: 2/19/2026, 5:58:05 PM
1class Solution(object):
2    def longestPalindrome(self, s):
3        """
4        :type s: str
5        :rtype: str
6        """
7        res = ""
8        resLen = 0
9        
10        for i in range(len(s)):
11            # Odd length palindromes (e.g., "aba")
12            l, r = i, i
13            while l >= 0 and r < len(s) and s[l] == s[r]:
14                if (r - l + 1) > resLen:
15                    res = s[l:r+1]
16                    resLen = r - l + 1
17                l -= 1
18                r += 1
19                
20            # Even length palindromes (e.g., "abba")
21            l, r = i, i + 1
22            while l >= 0 and r < len(s) and s[l] == s[r]:
23                if (r - l + 1) > resLen:
24                    res = s[l:r+1]
25                    resLen = r - l + 1
26                l -= 1
27                r += 1
28                
29        return res