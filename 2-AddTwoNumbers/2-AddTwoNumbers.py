# Last updated: 2/18/2026, 11:00:19 PM
1class Solution(object):
2    def addTwoNumbers(self, l1, l2):
3        """
4        :type l1: ListNode
5        :type l2: ListNode
6        :rtype: ListNode
7        """
8        # Create a placeholder to build the new list
9        dummy = ListNode(0)
10        curr = dummy
11        carry = 0
12        
13        # Keep going if there are nodes left OR a leftover carry
14        while l1 or l2 or carry:
15            # Get values, defaulting to 0 if list is exhausted
16            v1 = l1.val if l1 else 0
17            v2 = l2.val if l2 else 0
18            
19            # Calculate new digit and carry
20            total = v1 + v2 + carry
21            carry = total // 10
22            val = total % 10
23            
24            # Add new node to the result list
25            curr.next = ListNode(val)
26            
27            # Move pointers forward
28            curr = curr.next
29            if l1: l1 = l1.next
30            if l2: l2 = l2.next
31            
32        return dummy.next