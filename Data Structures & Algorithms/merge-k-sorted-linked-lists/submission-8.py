# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    
        if lists == []:
            return None

        dummy = ListNode(0, None)
        curr = dummy

        kListPointers = []
        
        for l in lists:
            kListPointers.append(l)


        kNulls = 0
        
        while kListPointers != []:
            index_to_advance = None
            number_to_add = float('inf')
            

            for i, pointer in enumerate(kListPointers):
                if pointer == None:
                    break
                elif pointer.val < number_to_add:
                    print(f"i: {i} | pointer.val : {pointer.val}")
                    number_to_add = pointer.val
                    index_to_advance = i
            
            if pointer == None:
                del kListPointers[i]

            elif index_to_advance != None:
                kListPointers[index_to_advance] = kListPointers[index_to_advance].next
                curr.next = ListNode(number_to_add, None)
                curr = curr.next


        return dummy.next
                
