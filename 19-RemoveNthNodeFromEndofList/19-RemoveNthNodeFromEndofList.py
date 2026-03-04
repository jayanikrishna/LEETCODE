# Last updated: 3/4/2026, 8:12:13 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6
7class Solution:
8    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
9        # Step 1: Create a dummy node to simplify edge cases
10        dummy = ListNode(0, head)
11        left = dummy
12        right = head
13        
14        # Step 2: Move the right pointer n steps ahead
15        while n > 0 and right:
16            right = right.next
17            n -= 1
18            
19        # Step 3: Move both pointers until right reaches the end
20        while right:
21            left = left.next
22            right = right.next
23            
24        # Step 4: Delete the node (skip it)
25        left.next = left.next.next
26        
27        # Step 5: Return the actual head
28        return dummy.next