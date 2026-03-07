# Last updated: 3/7/2026, 11:51:16 PM
1class Solution:
2    def removeElement(self, nums: list[int], val: int) -> int:
3        # k keeps track of the position for the next valid element
4        k = 0
5        
6        for i in range(len(nums)):
7            # If the current element is NOT the one we want to remove
8            if nums[i] != val:
9                # Move it to the front at position k
10                nums[k] = nums[i]
11                # Increment k to the next available slot
12                k += 1
13                
14        # k now represents the number of elements not equal to val
15        return k