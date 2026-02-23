# Last updated: 2/23/2026, 11:23:45 PM
1class Solution:
2    def reverse(self, x: int) -> int:
3        # Step 1: Determine the sign
4        sign = -1 if x < 0 else 1
5        x = abs(x)
6        
7        # Step 2: Reverse the string representation of the number
8        res = int(str(x)[::-1]) * sign
9        
10        # Step 3: Check for 32-bit overflow
11        # Range is [-2^31, 2^31 - 1]
12        if res < -2**31 or res > 2**31 - 1:
13            return 0
14            
15        return res