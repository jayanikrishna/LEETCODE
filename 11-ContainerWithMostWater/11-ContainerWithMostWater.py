# Last updated: 3/1/2026, 10:58:32 PM
1class Solution:
2    def maxArea(self, height: list[int]) -> int:
3        # Initialize two pointers at the ends of the array
4        l = 0
5        r = len(height) - 1
6        max_area = 0
7        
8        while l < r:
9            # Calculate the current width
10            width = r - l
11            
12            # The height of the container is the shorter of the two lines
13            current_height = min(height[l], height[r])
14            
15            # Update max_area if the current one is larger
16            max_area = max(max_area, width * current_height)
17            
18            # Move the pointer that points to the shorter line
19            if height[l] < height[r]:
20                l += 1
21            else:
22                r -= 1
23                
24        return max_area