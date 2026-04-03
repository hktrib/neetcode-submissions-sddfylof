# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        fast, slow = head, head

        while fast != None and fast.next != None:
            fast = fast.next.next
            slow = slow.next
        
        
        # The middle ListNode is always at the end of the list after 
        # reordering. Thus, it doesn't need to be touched.
        middle = slow

        print(f"middle: {middle.val}")

        stack = []

        temp = slow.next
        slow.next = None
        while temp != None:
            removeEdge = temp.next
            temp.next = None
            stack.append(temp)
            temp = None
            temp = removeEdge

        print(f"Stack")
        for elem in stack:
            print(f"val: {elem.val}")

        
        curr = head

        pos = 0

        # print(f"Middle: {middle} | {middle.val}")
        while stack != []:
            # print(f"Curr: {curr} | {curr.val}")
            if pos % 2 == 0:
                # print("Hit")
                elem_to_add = stack.pop()

                temp = curr.next

                curr.next = elem_to_add
                elem_to_add.next = temp
            
            curr = curr.next
            pos += 1


        return head
            

        

        


        


        

        
