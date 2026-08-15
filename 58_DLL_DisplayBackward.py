class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

def DisplayBackward(tail):
    curr = tail

    while curr is not None:
        print(curr.data, end = ' ')
        if curr.prev is not None:
            print("<->", end = ' ')
        curr = curr.prev

   

def DisplayForward(head):
    curr = head

    while curr is not None:
        print(curr.data, end = ' ')
        if curr.next is not None:
            print("<->", end = ' ')
        curr = curr.next
    print()

def main():
    head = Node(1)
    second = Node(2)
    third = Node(3)
    fourth = Node(4)

    head.next = second
    second.prev = head
    second.next = third
    third.prev = second
    third.next = fourth
    fourth.prev = third

    print("Forward Traversal: ", end = '')
    DisplayForward(head)

    print("Backward Traversal: ", end = '')
    DisplayBackward(fourth)

if __name__ == "__main__":
    main()