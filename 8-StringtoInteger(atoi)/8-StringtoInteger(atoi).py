# Last updated: 2/23/2026, 11:24:09 PM
1class Solution:
2    def isPalindrome(self, x: int) -> bool:
3        # Convert to string and compare with its reverse
4        return str(x) == str(x)[::-1]