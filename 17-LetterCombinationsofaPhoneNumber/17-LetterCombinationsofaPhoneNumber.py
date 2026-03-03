# Last updated: 3/3/2026, 10:55:45 PM
1class Solution:
2    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
3        nums.sort()
4        results = []
5        n = len(nums)
6        
7        for i in range(n - 3):
8            # Skip duplicate for the first number
9            if i > 0 and nums[i] == nums[i - 1]:
10                continue
11            
12            # Optimization: If the smallest 4 numbers are > target, stop
13            if nums[i] + nums[i+1] + nums[i+2] + nums[i+3] > target:
14                break
15            # Optimization: If the largest 3 numbers with nums[i] < target, skip i
16            if nums[i] + nums[n-3] + nums[n-2] + nums[n-1] < target:
17                continue
18
19            for j in range(i + 1, n - 2):
20                # Skip duplicate for the second number
21                if j > i + 1 and nums[j] == nums[j - 1]:
22                    continue
23                
24                l, r = j + 1, n - 1
25                while l < r:
26                    curr_sum = nums[i] + nums[j] + nums[l] + nums[r]
27                    
28                    if curr_sum == target:
29                        results.append([nums[i], nums[j], nums[l], nums[r]])
30                        l += 1
31                        r -= 1
32                        # Skip duplicates for the third and fourth numbers
33                        while l < r and nums[l] == nums[l - 1]:
34                            l += 1
35                        while l < r and nums[r] == nums[r + 1]:
36                            r -= 1
37                    elif curr_sum < target:
38                        l += 1
39                    else:
40                        r -= 1
41                        
42        return results