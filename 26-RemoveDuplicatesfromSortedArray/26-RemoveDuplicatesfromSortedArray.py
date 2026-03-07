# Last updated: 3/7/2026, 11:53:33 PM
1class Solution:
2    def divide(self, dividend: int, divisor: int) -> int:
3        # Step 1: Handle 32-bit overflow cases
4        MAX = 2**31 - 1
5        MIN = -2**31
6        
7        if dividend == MIN and divisor == -1:
8            return MAX
9        
10        # Step 2: Determine sign
11        negative = (dividend < 0) != (divisor < 0)
12        a, b = abs(dividend), abs(divisor)
13        res = 0
14        
15        # Step 3: Exponential subtraction
16        while a >= b:
17            temp_divisor, multiple = b, 1
18            # Keep doubling the divisor while it's smaller than the remainder
19            while a >= (temp_divisor << 1):
20                temp_divisor <<= 1
21                multiple <<= 1
22            
23            # Subtract the largest found multiple and update quotient
24            a -= temp_divisor
25            res += multiple
26            
27        # Step 4: Apply sign and clamp to 32-bit range
28        res = -res if negative else res
29        return max(MIN, min(MAX, res))