# Last updated: 2/18/2026, 11:01:25 PM
1class Solution(object):
2    def lengthOfLongestSubstring(self, s):
3        """
4        :type s: str
5        :rtype: int
6        """
7        char_map = {}
8        left = 0
9        max_len = 0
10        
11        for right in range(len(s)):
12            char = s[right]
13            
14            # If we find a duplicate in the current window
15            if char in char_map and char_map[char] >= left:
16                # Move left pointer to the right of the previous occurrence
17                left = char_map[char] + 1
18            
19            # Update the last seen index of the character
20            char_map[char] = right
21            
22            # Calculate window size and update max
23            max_len = max(max_len, right - left + 1)
24            
25        return max_len