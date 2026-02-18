# Last updated: 2/18/2026, 10:59:04 PM
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Dictionary to store: { value : index }
        prev_map = {} 
        
        for i, n in enumerate(nums):
            # Calculate what number we need to reach the target
            diff = target - n
            
            # If that number is already in our dictionary, we found the pair
            if diff in prev_map:
                return [prev_map[diff], i]
            
            # Otherwise, add the current number and its index to the map
            prev_map[n] = i
            
        return []