# Last updated: 2/22/2026, 11:24:15 PM
1class Solution:
2    def containsDuplicate(self, nums: list[int]) -> bool:
3        return len(nums) != len(set(nums))