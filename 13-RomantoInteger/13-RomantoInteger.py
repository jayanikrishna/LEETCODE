# Last updated: 3/1/2026, 11:01:06 PM
1class Solution:
2    def romanToInt(self, s: str) -> int:
3        # Step 1: Create a dictionary for symbol-to-value lookup
4        roman_map = {
5            'I': 1,
6            'V': 5,
7            'X': 10,
8            'L': 50,
9            'C': 100,
10            'D': 500,
11            'M': 1000
12        }
13        
14        total = 0
15        n = len(s)
16        
17        # Step 2: Iterate through the string
18        for i in range(n):
19            current_val = roman_map[s[i]]
20            
21            # Check if we are at the last character or if the current symbol 
22            # is smaller than the next one
23            if i + 1 < n and current_val < roman_map[s[i + 1]]:
24                # Subtractive case
25                total -= current_val
26            else:
27                # Additive case
28                total += current_val
29                
30        return total