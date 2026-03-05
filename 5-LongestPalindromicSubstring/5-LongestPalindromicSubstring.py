# Last updated: 3/6/2026, 12:13:05 AM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6
7class Solution:
8    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
9        dummy = ListNode(0, head)
10        groupPrev = dummy
11        
12        while True:
13            # 1. Find the kth node from groupPrev
14            kth = self.getKth(groupPrev, k)
15            if not kth:
16                break
17            groupNext = kth.next
18            
19            # 2. Reverse the group (between groupPrev and groupNext)
20            prev, curr = kth.next, groupPrev.next
21            while curr != groupNext:
22                tmp = curr.next
23                curr.next = prev
24                prev = curr
25                curr = tmp
26            
27            # 3. Re-link the reversed group to the rest of the list
28            tmp = groupPrev.next
29            groupPrev.next = kth
30            groupPrev = tmp
31            
32        return dummy.next
33    
34    def getKth(self, curr, k):
35        while curr and k > 0:
36            curr = curr.next
37            k -= 1
38        return curr