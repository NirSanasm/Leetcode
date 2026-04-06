1class Solution:
2    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
3        
4        dummy = ListNode()
5        res = dummy
6
7        total = carry = 0
8
9        while l1 or l2 or carry:
10            total = carry
11
12            if l1:
13                total += l1.val
14                l1 = l1.next
15            if l2:
16                total += l2.val
17                l2 = l2.next
18            
19            num = total % 10
20            carry = total // 10
21            dummy.next = ListNode(num)
22            dummy = dummy.next
23        
24        return res.next