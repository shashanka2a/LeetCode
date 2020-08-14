"""
Given a sorted linked list, delete all duplicates such that each element appear only once.

Example 1:

Input: 1->1->2
Output: 1->2
Example 2:

Input: 1->1->2->3->3
Output: 1->2->3
"""


def deleteDuplicates(self, head: ListNode) -> ListNode:
    if not head: return None
    curr = head
    seen = {}
    while(curr is not None and curr.next is not None):
        if curr.val not in seen:
            seen[curr.val] = 1 
        if curr.next.val in seen:
            curr.next = curr.next.next
        else:
            curr = curr.next
    return head
