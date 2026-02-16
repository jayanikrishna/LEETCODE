# Last updated: 2/16/2026, 11:40:58 PM
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        
        while left <= right:
            # Finding the middle index
            mid = left + (right - left) // 2
            
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                # Target is in the right half, discard left half
                left = mid + 1
            else:
                # Target is in the left half, discard right half
                right = mid - 1
                
        # If we exit the loop, the target was not in the array
        return -1