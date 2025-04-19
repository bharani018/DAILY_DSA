class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def lengthLL(head: ListNode)->int:
    length = 0
    current = head
    while current:
        length+=1
        current = current.next
    return length

def list_to_linkedlist(items):
    dummy = ListNode()
    current = dummy
    for val in items:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

l = [5,3,4,1,2]
head = list_to_linkedlist(l)

print(lengthLL(head))

def sortLL(head: ListNode) -> int:
    if not head or not head.next:
        return head
    
    swapped = True
    
    while swapped:
        swapped = False
        current = head

        while current and current.next:
            if current.val > current.next.val:
                current.val, current.next.val = current.next.val, current.val
                swapped = True
            current = current.next
    return head

def printLL(head: ListNode):
    curr = head
    while curr:
        print(curr.val, end="->")
        curr=curr.next
    print("None")



printLL(sortLL(head))


