# Last updated: 3/7/2026, 11:49:47 PM
1class Solution:
2    def removeDuplicates(self, nums: list[int]) -> int:
3        if not nums:
4            return 0
5        
6        # 'i' is the pointer for the last unique element found
7        i = 0
8        
9        # 'j' is the explorer pointer
10        for j in range(1, len(nums)):
11            # If we find a value different from our last unique value
12            if nums[j] != nums[i]:
13                # Move the unique pointer forward
14                i += 1
15                # Update the unique position with the new value
16                nums[i] = nums[j]
17        
18        # Return the count of unique elements (index + 1)
19        return i + 1
20        