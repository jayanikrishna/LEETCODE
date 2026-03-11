# Last updated: 3/11/2026, 11:44:25 PM
1class Solution:
2    def nextPermutation(self, nums: List[int]) -> None:
3        n = len(nums)
4        pivot = -1
5        
6        # Step 1: Find the pivot (first decreasing element from the right)
7        for i in range(n - 2, -1, -1):
8            if nums[i] < nums[i + 1]:
9                pivot = i
10                break
11        
12        if pivot != -1:
13            # Step 2: Find the successor to the pivot
14            for i in range(n - 1, pivot, -1):
15                if nums[i] > nums[pivot]:
16                    nums[i], nums[pivot] = nums[pivot], nums[i]
17                    break
18        
19        # Step 3: Reverse the elements after the pivot
20        # If pivot is -1, this reverses the entire array (correct for [3,2,1])
21        left, right = pivot + 1, n - 1
22        while left < right:
23            nums[left], nums[right] = nums[right], nums[left]
24            left += 1
25            right -= 1