

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def list_to_linkedlist(items):
    dummy = ListNode()
    curr = dummy
    for i in items:
        curr.next = ListNode(i)
        curr = curr.next
    return dummy.next


def removeNthnode(head: ListNode, n: int):
    lenth = 0
    curr = head
    while curr:
        lenth +=1
        curr= curr.next
    nthNode = lenth - n 

    dummy = ListNode()
    dummy.next = head
    current = dummy

    
    for i in range(nthNode):
        current = current.next
    current.next = current.next.next
    return dummy.next

def printLL(head: ListNode):
    curr = head
    while curr:
        print(curr.val, end="->")
        curr = curr.next
    print(None)
head = list_to_linkedlist([1,2,3,4,5])
printLL(removeNthnode(head, 2))

