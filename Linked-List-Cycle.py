1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, x):
4#         self.val = x
5#         self.next = None
6
7class Solution:
8    def hasCycle(self, head):
9        
10        if not head or not head.next:
11            return False
12
13        
14        slow = head
15        fast = head
16
17        
18        while fast and fast.next:
19            slow = slow.next         
20            fast = fast.next.next     
21
22            
23            if slow == fast:
24                return True
25
26        
27        return False
28        
29
30