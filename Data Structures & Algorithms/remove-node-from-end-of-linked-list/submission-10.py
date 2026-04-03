# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        # dummy = ListNode(0, head)
        right = head
        left = ListNode(0, head) # dummy node idea


        while n > 0:
            right = right.next
            n -= 1

        
        while right:
            right = right.next
            left = left.next


        temp = left.next
        left.next = left.next.next

        if temp == head:
            head = head.next
            temp.next = None
            temp = None

        return head
