# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        num1 = 0
        num2 = 0

        dummyNode = ListNode(0, None)

        multiplier = 1
        while l1:
            num1 += l1.val * multiplier

            multiplier *= 10

            l1 = l1.next


        multiplier = 1
        while l2:
            num1 += l2.val * multiplier

            multiplier *= 10

            l2 = l2.next
        
        sumLL = num1 + num2

        if sumLL == 0:
            return ListNode(0)

        curr = dummyNode
        while sumLL != 0:
            print(f"sumLL: {sumLL}")
            print(f"sumLL % 10: {sumLL % 10}")
            curr.next = ListNode(sumLL % 10, None)
            curr = curr.next
            sumLL //= 10
        
        return dummyNode.next
        