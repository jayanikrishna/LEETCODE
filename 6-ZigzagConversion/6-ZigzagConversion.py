# Last updated: 2/19/2026, 5:59:09 PM
1class Solution(object):
2    def convert(self, s, numRows):
3        """
4        :type s: str
5        :type numRows: int
6        :rtype: str
7        """
8        # If there's only 1 row, or the string can't fill rows, return as is
9        if numRows == 1 or numRows >= len(s):
10            return s
11        
12        # Create a list for each row
13        rows = [[] for _ in range(numRows)]
14        
15        current_row = 0
16        step = 1  # 1 means moving down, -1 means moving up
17        
18        for char in s:
19            rows[current_row].append(char)
20            
21            # If we hit the top row, start moving down
22            if current_row == 0:
23                step = 1
24            # If we hit the bottom row, start moving up
25            elif current_row == numRows - 1:
26                step = -1
27            
28            current_row += step
29            
30        # Combine all characters in each row, then join the rows
31        return "".join(["".join(row) for row in rows])