"""
Given a linked list, determine if it has a cycle in it.

To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.

Example 1:

Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where tail connects to the second node.
"""


def hasCycle(self, head: ListNode) -> bool:
    slow,fast = head,head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow==fast:
            return True
    return False

def hasCycleAlernate(self, head: ListNode) -> bool:
    while head:
        if head.val == float(inf):
            return True
        head.val = float(inf)
        head = head.next
    return False
