class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None

def addTwoNumbers(l1:ListNode,l2:ListNode):
    l1pointer = l1
    l2pointer = l2
    c = 0
    if l1 == None or l2== None:
        return None
    while l1pointer.next != None and l2pointer.next != None:
        l1pointer.val += l2pointer.val + c
        c,l1pointer.val =divmod(l1pointer.val,10)
        l1pointer = l1pointer.next
        l2pointer = l2pointer.next

    if l2pointer.next != None:
        l1pointer.next = l2pointer.next

    l1pointer.val += l2pointer.val + c
    c, l1pointer.val = divmod(l1pointer.val, 10)

    while l1pointer.next != None:
        l1pointer = l1pointer.next
        l1pointer.val += c
        c,l1pointer.val = divmod(l1pointer.val, 10)

    if c != 0:
        l1pointer.next = ListNode(1)
    return l1
if __name__ == '__main__':
    l1 = ListNode(1)
    l1.next = ListNode(2)
    l1.next.next = ListNode(3)
    l2 = ListNode(9)
    # l2.next = ListNode(9)
    # l2.next.next = ListNode(9)
    result = addTwoNumbers(l1,l2)
    while result is not None:
        print(result.val)
        result = result.next