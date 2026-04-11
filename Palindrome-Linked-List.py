1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def reverse(self, head: ListNode) -> ListNode:
8        prev = None
9        curr = head
10        while curr:
11            next_temp = curr.next
12            curr.next = prev
13            prev = curr
14            curr = next_temp
15        return prev
16
17    def isPalindrome(self, head: Optional[ListNode]) -> bool:
18        slow = head
19        fast = head
20        while fast and fast.next:
21            slow = slow.next
22            fast = fast.next.next
23        rev = self.reverse(slow)
24        while rev:
25            if head.val != rev.val:
26                return False
27            head = head.next
28            rev = rev.next
29        return True