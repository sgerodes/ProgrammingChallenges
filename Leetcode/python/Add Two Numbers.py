# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        weight=0
        number=0
        while l1 != None or l2 != None:
            if l1:
                number+= l1.val*10**weight
                l1=l1.next
            if l2:
                number+= l2.val*10**weight
                l2=l2.next
            weight+=1
        dummy=ListNode(-1000)
        curr=dummy
        for digit in str(number)[::-1]:
            curr.next=ListNode(int(digit))
            curr=curr.next
        return dummy.next





