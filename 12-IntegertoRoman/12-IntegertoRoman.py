# Last updated: 3/1/2026, 10:59:32 PM
1class Solution:
2    def intToRoman(self, num: int) -> str:
3        # Define the mapping of values to Roman symbols in descending order
4        # Including the subtractive cases (4, 9, 40, etc.) makes the logic much simpler
5        sym_map = [
6            (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
7            (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
8            (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
9        ]
10        
11        res = []
12        
13        for value, symbol in sym_map:
14            # We skip values that are larger than our current num
15            if num == 0: break
16            
17            # Find how many times this symbol fits into the current num
18            count = num // value
19            if count > 0:
20                res.append(symbol * count)
21                # Reduce num by the total value we just added to the result
22                num -= (value * count)
23                
24        return "".join(res)