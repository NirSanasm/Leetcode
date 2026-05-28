1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, x):
4#         self.val = x
5#         self.next = None
6
7class Solution:
8    def deleteNode(self, node):
9        """
10        :type node: ListNode
11        :rtype: void Do not return anything, modify node in-place instead.
12        """
13        node.val = node.next.val
14        node.next = node.next.next
15        