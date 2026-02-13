// Last updated: 2/13/2026, 12:39:22 PM
#include <vector>
#include <algorithm>
#include <climits>

using namespace std;

class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        // Ensure nums1 is the smaller array to keep complexity O(log(min(m, n)))
        if (nums1.size() > nums2.size()) {
            return findMedianSortedArrays(nums2, nums1);
        }

        int m = nums1.size();
        int n = nums2.size();
        int low = 0, high = m;

        while (low <= high) {
            int partitionX = low + (high - low) / 2;
            int partitionY = (m + n + 1) / 2 - partitionX;

            // If partitionX is 0, nothing on left. Use INT_MIN for comparison.
            int maxLeftX = (partitionX == 0) ? INT_MIN : nums1[partitionX - 1];
            // If partitionX is m, nothing on right. Use INT_MAX for comparison.
            int minRightX = (partitionX == m) ? INT_MAX : nums1[partitionX];

            int maxLeftY = (partitionY == 0) ? INT_MIN : nums2[partitionY - 1];
            int minRightY = (partitionY == n) ? INT_MAX : nums2[partitionY];

            if (maxLeftX <= minRightY && maxLeftY <= minRightX) {
                // We have partitioned the combined array into two halves correctly
                if ((m + n) % 2 == 0) {
                    return (max(maxLeftX, maxLeftY) + min(minRightX, minRightY)) / 2.0;
                } else {
                    return max(maxLeftX, maxLeftY);
                }
            } 
            else if (maxLeftX > minRightY) {
                // We are too far right in nums1, move left
                high = partitionX - 1;
            } 
            else {
                // We are too far left in nums1, move right
                low = partitionX + 1;
            }
        }
        
        return 0.0; // Should never reach here for valid sorted inputs
    }
};