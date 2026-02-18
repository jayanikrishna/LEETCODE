# Last updated: 2/18/2026, 10:58:48 PM
1class Solution(object):
2    def twoSum(self, nums, target):
3        """
4        :type nums: List[int]
5        :type target: int
6        :rtype: List[int]
7        """
8        # Dictionary to store: { value : index }
9        prev_map = {} 
10        
11        for i, n in enumerate(nums):
12            # Calculate what number we need to reach the target
13            diff = target - n
14            
15            # If that number is already in our dictionary, we found the pair
16            if diff in prev_map:
17                return [prev_map[diff], i]
18            
19            # Otherwise, add the current number and its index to the map
20            prev_map[n] = i
21            
22        return []