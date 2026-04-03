# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        head = curr = None

        while list1 != None and list2 != None:
            newNode = None
            if list1.val < list2.val:
                newNode = ListNode(list1.val, None)
                list1 = list1.next
            elif list2.val <= list1.val:
                newNode = ListNode(list2.val, None)
                list2 = list2.next
            
            if head == None:
                head = curr = newNode 
            else:
                curr.next = newNode
                curr = newNode
        
        if head != None:
            if list1 == None:
                curr.next = list2
            else:
                curr.next = list1
        else:
            if list1 == None:
                head = list2
            else:
                head = list1


        return head