"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""

def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
    dummy = ListNode(0)
    cur = dummy
    carry = 0
    while l1 or l2:
        sums = 0
        if l1:
            sums += l1.val
            l1 = l1.next
        if l2:
            sums += l2.val
            l2 = l2.next
        sums += carry
        cur.next = ListNode(sums%10)
        cur = cur.next
        carry = sums//10
    if carry:
        cur.next = ListNode(carry)

    return dummy.next
