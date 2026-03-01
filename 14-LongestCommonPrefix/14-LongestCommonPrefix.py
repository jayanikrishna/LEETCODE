# Last updated: 3/1/2026, 11:03:03 PM
1class Solution:
2    def longestCommonPrefix(self, strs: list[str]) -> str:
3        # If the input list is empty (though constraints say 1 <= len)
4        if not strs:
5            return ""
6        
7        # Take the first string as the reference
8        first = strs[0]
9        
10        for i in range(len(first)):
11            char = first[i]
12            
13            # Check this character against the same position in all other strings
14            for j in range(1, len(strs)):
15                # If we've reached the end of another string OR found a mismatch
16                if i == len(strs[j]) or strs[j][i] != char:
17                    # Return the portion of the first string we've matched so far
18                    return first[:i]
19        
20        # If we finish the loop, the entire first string is the prefix
21        return first
22        