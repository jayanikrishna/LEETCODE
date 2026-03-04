# Last updated: 3/4/2026, 8:14:40 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6
7class Solution:
8    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
9        # Step 1: Create a dummy node to act as the start
10        dummy = ListNode()
11        tail = dummy
12        
13        # Step 2: Traverse both lists
14        while list1 and list2:
15            if list1.val < list2.val:
16                tail.next = list1
17                list1 = list1.next
18            else:
19                tail.next = list2
20                list2 = list2.next
21            tail = tail.next
22            
23        # Step 3: Attach the remaining nodes from whichever list isn't empty
24        if list1:
25            tail.next = list1
26        elif list2:
27            tail.next = list2
28            
29        # Step 4: Return the head (ignoring the dummy node)
30        return dummy.next