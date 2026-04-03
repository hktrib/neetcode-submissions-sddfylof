# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        list_len = 0

        while curr != None:
            curr = curr.next
            list_len += 1

        nthNode = list_len - n


        if list_len == 1 or nthNode == 0:
            temp = head.next
            head.next = None
            return temp
        else:
            curr = head
            prev = None
            i = 0


            print(f"nthNode: {nthNode}")
            print(f"n: {n}")
            print(f"list_len: {list_len}")
            while i <= nthNode and curr != None:

                print(f"curr: {curr.val}")
                if i == nthNode:
                    prev.next = curr.next
                    curr.next = None
                    curr = None
                    
                    return head

                prev = curr
                curr = curr.next
                i += 1

        return head