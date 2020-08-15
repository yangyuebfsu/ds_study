***
21. Merge Two Sorted Lists

Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4

***

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(float("-inf"))  # a dummy node
        cur = dummy
        while l1 and l2:
            if l1.val <= l2.val:  # sorted
                cur.next = l1
                l1 = l1.next  # go ahead
            else:
                cur.next = l2
                l2 = l2.next  # go ahead
            cur = cur.next  # go ahead
        # when one of them is None, cur should point at the remainder since the linked lists are sorted
        cur.next = l1 if l1 else l2
        return dummy.next
