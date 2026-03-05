# Last updated: 3/6/2026, 12:09:58 AM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6
7class Solution:
8    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
9        # Step 1: Initialize dummy node
10        dummy = ListNode(0, head)
11        prev = dummy
12        curr = head
13        
14        # Step 2: Iterate while there are at least two nodes to swap
15        while curr and curr.next:
16            # Nodes to be swapped
17            first = curr
18            second = curr.next
19            
20            # Step 3: Re-wire the pointers
21            # 1. Point the previous node to the second node
22            prev.next = second
23            # 2. Point the first node to the node after the second
24            first.next = second.next
25            # 3. Point the second node back to the first
26            second.next = first
27            
28            # Step 4: Move pointers forward for the next pair
29            prev = first
30            curr = first.next
31            
32        return dummy.next