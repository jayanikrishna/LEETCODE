# Last updated: 3/3/2026, 10:52:03 PM
1class Solution:
2    def threeSum(self, nums: list[int]) -> list[list[int]]:
3        res = []
4        nums.sort()  # Sorting is key for the two-pointer approach
5        
6        for i in range(len(nums)):
7            # If the current value is > 0, no 3 numbers can sum to 0 anymore
8            if nums[i] > 0:
9                break
10            
11            # Skip the same element to avoid duplicate triplets
12            if i > 0 and nums[i] == nums[i - 1]:
13                continue
14            
15            # Two-pointer initialization
16            l, r = i + 1, len(nums) - 1
17            while l < r:
18                three_sum = nums[i] + nums[l] + nums[r]
19                
20                if three_sum > 0:
21                    r -= 1
22                elif three_sum < 0:
23                    l += 1
24                else:
25                    res.append([nums[i], nums[l], nums[r]])
26                    l += 1
27                    r -= 1
28                    # Skip duplicate values for the left pointer
29                    while nums[l] == nums[l - 1] and l < r:
30                        l += 1
31                        
32        return res