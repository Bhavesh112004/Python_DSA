class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def getKthFromLast(head, k):
    slow = head 
    fast = head

    while k>0:
        if fast is None:
            return -1
        fast = fast.next
        k -= 1

    while fast is not None:
        slow = slow.next
        fast = fast.next

    return slow.data if slow is not None else -1

if __name__ == '__main__':
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    head.next.next.next.next.next.next = Node(7)
    head.next.next.next.next.next.next.next = Node(8)
    head.next.next.next.next.next.next.next.next = Node(9)

    k = 4

    print(getKthFromLast(head, k))