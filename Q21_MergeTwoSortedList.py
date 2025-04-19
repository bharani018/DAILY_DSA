

class ListNode:
    def __init__(self, val=0, next = None):
        self.val = val
        self.next = next

def MergeTwoList(l1: ListNode, l2:ListNode):
    if not l1:
        return l2
    if not l2:
        return l1
    res = ListNode()
    curr = res

    while l1 and l2:
        if l1.val<l2.val:
            curr.next = l1
            l1 = l1.next
        else:
            curr.next = l2
            l2 = l2.next
        curr = curr.next
        if l1:
            curr.next = l1
        elif l2:
            curr.next = l2

    return res.next

list1 = [0]
list2 = []

def list_to_LL(items):
    dummy = ListNode()
    curr = dummy
    for i in items:
        curr.next = ListNode(i)
        curr = curr.next
    return dummy.next

l1 = list_to_LL(list1)
l2 = list_to_LL(list2)

def printLL(res: ListNode):
    curr = res
    while curr:
        print(curr.val, end="->")
        curr = curr.next
    print(None)

printLL(MergeTwoList(l1, l2))