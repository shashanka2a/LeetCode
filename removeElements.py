"""
Remove all elements from a linked list of integers that have value val.

Example:

Input:  1->2->6->3->4->5->6, val = 6
Output: 1->2->3->4->5
"""

def removeElements(self, head: ListNode, val: int) -> ListNode:
    dummy = ListNode("Filler")
    dummy.next = head
    curr = dummy
    while curr:
        if curr.next and curr.next.val == val:
            curr.next = curr.next.next
        else:
            curr = curr.next
    return dummy.next
