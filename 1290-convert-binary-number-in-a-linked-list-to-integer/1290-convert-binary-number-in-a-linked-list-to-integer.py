# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        res=0
        binary=[]
        while head is not None:
            binary.append(head.val)
            head=head.next
        binary=binary[::-1]
        for i in range(len(binary)):
            res+= int(binary[i]) * pow(2,i)
        return res


        