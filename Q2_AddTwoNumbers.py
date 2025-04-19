
class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next
    

def AddTwoNums(l1: ListNode, l2: ListNode):
    res = ListNode()
    current = res
    cur1 = l1
    cur2 = l2
    tot = 0
    while cur1 or cur2:
        val1 = cur1.val if cur1 else 0
        val2 = cur2.val if cur2 else 0
        tot += val1 + val2
        if(tot<=9):
            current.next = ListNode(tot)
            current = current.next
            if cur1:
                cur1 = cur1.next
            if cur2:
                cur2 = cur2.next
            tot =0
        else:
            tot%=10
            current.next = ListNode(tot)
            current = current.next
            if cur1:
                cur1 = cur1.next
            if cur2:
                cur2 = cur2.next
            tot = 1
            current.next = ListNode(1)

    return res.next

def list_to_LL(items):
    dummy = ListNode()
    current = dummy
    for i in items:
        current.next = ListNode(i)
        current = current.next
    return dummy.next

l1 = list_to_LL([9,9,9,9,9,9,9])
l2 = list_to_LL([9,9,9,9])

def printLL(res: ListNode):
    curr = res
    while curr:
        print(curr.val, end="->")
        curr = curr.next
    print(None)


printLL(AddTwoNums(l1, l2))
