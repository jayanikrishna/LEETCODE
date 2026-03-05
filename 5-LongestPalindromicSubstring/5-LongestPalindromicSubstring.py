# Last updated: 3/6/2026, 12:08:23 AM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6
7class Solution:
8    def mergeKLists(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:
9        if not lists or len(lists) == 0:
10            return None
11        
12        while len(lists) > 1:
13            merged_lists = []
14            
15            # Pair up lists and merge them
16            for i in range(0, len(lists), 2):
17                l1 = lists[i]
18                l2 = lists[i + 1] if (i + 1) < len(lists) else None
19                merged_lists.append(self.mergeTwoLists(l1, l2))
20            
21            # Update lists with the newly merged pairs
22            lists = merged_lists
23            
24        return lists[0]
25
26    def mergeTwoLists(self, l1, l2):
27        dummy = ListNode()
28        tail = dummy
29        
30        while l1 and l2:
31            if l1.val < l2.val:
32                tail.next = l1
33                l1 = l1.next
34            else:
35                tail.next = l2
36                l2 = l2.next
37            tail = tail.next
38        
39        tail.next = l1 or l2
40        return dummy.next