# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        # Create a dummy node as the head of the merged list
        dummy = ListNode(0)
        current = dummy
        
        # Compare the values of the nodes from both lists
        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
            
        # Append the remaining nodes from the non-empty list
        if list1:
            current.next = list1
        elif list2:
            current.next = list2
        # Return  the head of the merged list
        return dummy.next