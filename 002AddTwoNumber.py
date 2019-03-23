class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None

def addTwoNumbers(l1:ListNode,l2:ListNode):
    l1pointer = l1
    l2pointer = l2
    result = ListNode(l1.val+l2.val)
    resultpointer = result
    [c, resultpointer.val] = divmod(resultpointer.val, 10)
    l1pointer = l1pointer.next
    l2pointer = l2pointer.next
    while l1pointer != None and l2pointer != None:
        resultpointer.next = ListNode(l1pointer.val+l2pointer.val+c)
        resultpointer = resultpointer.next
        [c,resultpointer.val] = divmod(resultpointer.val,10)
        l1pointer = l1pointer.next
        l2pointer = l2pointer.next
    while l1pointer != None:
        resultpointer.next = ListNode(l1pointer.val+c)
        resultpointer = resultpointer.next
        [c,resultpointer.val] = divmod(resultpointer.val,10)
        l1pointer = l1pointer.next
    while l2pointer != None:
        resultpointer.next = ListNode(l2pointer.val + c)
        resultpointer = resultpointer.next
        [c,resultpointer.val] = divmod(resultpointer.val,10)
        l2pointer = l2pointer.next
    if c != 0:
        resultpointer.next = ListNode(1)
    return result

if __name__ == '__main__':
    l1 = ListNode(1)
    # l1.next = ListNode(2)
    # l1.next.next = ListNode(3)
    l2 = ListNode(9)
    l2.next = ListNode(9)
    result = addTwoNumbers(l1,l2)
    while result is not None:
        print(result.val)
        result = result.next