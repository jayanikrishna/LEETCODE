# Last updated: 2/16/2026, 11:41:20 PM
1class Solution(object):
2    def search(self, nums, target):
3        """
4        :type nums: List[int]
5        :type target: int
6        :rtype: int
7        """
8        left, right = 0, len(nums) - 1
9        
10        while left <= right:
11            # Finding the middle index
12            mid = left + (right - left) // 2
13            
14            if nums[mid] == target:
15                return mid
16            elif nums[mid] < target:
17                # Target is in the right half, discard left half
18                left = mid + 1
19            else:
20                # Target is in the left half, discard right half
21                right = mid - 1
22                
23        # If we exit the loop, the target was not in the array
24        return -1