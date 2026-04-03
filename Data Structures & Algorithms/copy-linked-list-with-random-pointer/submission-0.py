"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        dummyNode = Node(0, None)

        curr1 = head
        curr2 = dummyNode

        nodeMap = {None: None}

        while curr1:
            curr2.next = Node(curr1.val, None)

            curr2 = curr2.next
            nodeMap[curr1] = curr2

            curr1 = curr1.next

        curr1 = head
        curr2 = dummyNode.next

        while curr1:
            curr2.random = nodeMap[curr1.random]

            curr1 = curr1.next
            curr2 = curr2.next
        
        return dummyNode.next

