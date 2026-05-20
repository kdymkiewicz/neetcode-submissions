# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        stack = []
        while head:
            stack.append(head.val)
            head = head.next

        if stack:
            head = ListNode(stack.pop())
            node = head
            while stack:
                next_node = ListNode(stack.pop())
                node.next = next_node

                node = next_node

        return head