"""
Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You may not modify the values in the list's nodes, only nodes itself may be changed.

Example 1:

Given 1->2->3->4, reorder it to 1->4->2->3.
Example 2:

Given 1->2->3->4->5, reorder it to 1->5->2->4->3.
"""



def reorderList(self, head: ListNode) -> None:
    """
    Do not return anything, modify head in-place instead.
    """       
    if not head:
        return head

    slow = head
    fast = head

    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    second_head = self.reverseList(slow)
    slow.next = None
    self.merge_list(head,second_head)

def reverseList(self,head):
    prev = None
    curr = head
    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    return prev

def merge_list(self, a, b):
    while a and b:
        a.next, a = b, a.next
        b.next, b = a, b.next
