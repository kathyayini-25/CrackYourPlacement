class Solution:
    def sort(self, head):
        # return head
        arr=[]
        while head:
            arr.append(head.data)
            head=head.next
        arr.sort()
        dummy=Node(arr[0])
        curr=dummy
        for i in range(1,len(arr)):
            curr.next=Node(arr[i])
            curr=curr.next
        
        return dummy
