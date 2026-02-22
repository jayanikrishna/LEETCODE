# Last updated: 2/22/2026, 10:05:10 PM
1class Solution(object):
2    def myAtoi(self, s):
3        """
4        :type s: str
5        :rtype: int
6        """
7        # Define the 32-bit signed integer boundaries
8        MAX_INT = 2147483647
9        MIN_INT = -2147483648
10        
11        # 1. Strip leading whitespace
12        s = s.lstrip()
13        if not s:
14            return 0
15        
16        # 2. Determine the sign
17        sign = 1
18        i = 0
19        if s[i] == '-':
20            sign = -1
21            i += 1
22        elif s[i] == '+':
23            i += 1
24            
25        # 3. Read digits and convert
26        res = 0
27        while i < len(s) and s[i].isdigit():
28            digit = int(s[i])
29            
30            # 4. Check for overflow before updating the result
31            # 2147483647 // 10 is 214748364. 
32            # If res is greater, adding any digit overflows.
33            # If res is equal, adding a digit > 7 overflows.
34            if res > MAX_INT // 10 or (res == MAX_INT // 10 and digit > 7):
35                return MAX_INT if sign == 1 else MIN_INT
36            
37            res = res * 10 + digit
38            i += 1
39            
40        return res * sign